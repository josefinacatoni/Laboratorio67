# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig
from scipy.optimize import least_squares

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8  			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'legend.numpoints': 1,            # the number of points in the legend line
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)

def sliding_mean(data_array, window):
#    data_array = array(data_array)
    new_list = []
    for i in range(len(data_array)):
        indices = range(max(i - window + 1, 0),
                        min(i + window + 1, len(data_array)))
        avg = 0
        for j in indices:
            avg += data_array[j]
        avg /= float(len(indices))
        new_list.append(avg)

    return new_list



def sliding_median(data_array, window):
#    data_array = array(data_array)
    new_list = []
    for i in range(len(data_array)):
        indices = range(max(i - window + 1, 0),
                        min(i + window + 1, len(data_array)))

        med = np.median([data_array[j] for j in indices])
        new_list.append(med)

    return new_list

############ https://scipy-cookbook.readthedocs.io/items/robust_regression.html

def fun(x, t, y):
    return x[0] * (1.0 - np.exp(-x[1] * t)) - y

def generate_data(t, A, sigma, noise=0, n_outliers=0, random_state=0):
    y = A * (1.0 - np.exp(-sigma * t))
    rnd = np.random.RandomState(random_state)
    error = noise * rnd.randn(t.size)
    outliers = rnd.randint(0, t.size, n_outliers)
    error[outliers] *= 35
    return y + error

#################### DATA LAMMPS ##############################

data1= np.genfromtxt('./fig1_version1c_maximos.dat', delimiter = '\t')	

#################### PLOT specification ##############################

tiempo=data1[:,0]
vernier=data1[:,1]
sensor=data1[:,2]


x_test = np.linspace(0.0, 2.0, 100)

x0 = np.ones(2)
res_lsq = least_squares(fun, x0, args=(vernier,sensor))
y_lsq = generate_data(x_test,  *res_lsq.x)

x0 = np.ones(2)
res_robust = least_squares(fun, x0, loss='soft_l1', f_scale=0.1, args=(vernier,sensor))
y_robust = generate_data(x_test, *res_robust.x)

print(res_lsq.x)
print(res_robust.x)

#################### PLOT specification ##############################

fig=plt.figure(1)                # the first figure

ax1 = fig.add_subplot(111)
ax1.grid(False)


ax1.plot(vernier,sensor,'o',markersize=0.5,color='gray',label=r'Vernier sin el offset (mediana)')

ax1.plot(x_test,y_lsq,lw=0.4,linestyle='--',color='orange',label=r'ajuste LSQ')
ax1.plot(x_test,y_robust,lw=0.3,linestyle=':',color='firebrick',label=r'ajuste LSQ robusto')

ax1.text(0.1,2.0,r'y=A[1-exp(-Bx)]')
ax1.text(1.0 ,0.7 ,r'A=3.028 , B=0.916')


legend = plt.legend(loc='lower right',prop={'size':3.5})


ax1.set_ylim(0, 2.5)
#ax1.set_yticks(np.arange(-200,-40,40))
ax1.set_xlim(0, 2.0)
#ax1.set_xticks(np.arange(0,4,1))
#ax1.set_xlabel(r'$1/T$~(MeV$^{-1}$)')
#ax2.set_ylabel(r'$E_\mathrm{sym}$~(MeV)')
ax1.set_xlabel(r'Vernier-offset~(V)')
ax1.set_ylabel(r'Sensor-offset~(V)')
#ax2.set_ylabel(r'$\kappa$~(c/fm$^2$) (Nandi)')
ax1.set_title(r'Cuadrado bis')


pylab.savefig('fig1_version1c_maximos.eps', format='eps', dpi=300, bbox_inches='tight')



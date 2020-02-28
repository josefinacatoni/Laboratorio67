# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig

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
#    return array(new_list)  

def getKey(item):
    return item[0]

#################### DATA LAMMPS ##############################

data1= np.genfromtxt('./cuadradoS13.dat', delimiter = '\t')	
data2= np.genfromtxt('./cuadradoS13bis.dat', delimiter = '\t')	

data3= np.genfromtxt('./fig1_version1d.dat', delimiter = '\t')	#cuadradoS13.dat
data4= np.genfromtxt('./fig1_version1c.dat', delimiter = '\t')	#cuadradoS13bis.dat


#################### PLOT specification ##############################


tiempo=data3[:,0]
vernier=data3[:,1]
sensor=data3[:,2]

tiempo_bis=data4[:,0]
vernier_bis=data4[:,1]
sensor_bis=data4[:,2]


#mydata1=np.array(sorted(data1[19::20,2:4],key=getKey))


#################### PLOT specification ##############################

fig=plt.figure(1)                # the first figure

ax1 = fig.add_subplot(111)

#ax1.grid(color='gray', linestyle='--', linewidth=0.3,axis='both')
ax1.grid(False)
#ax2 = ax1.twinx()
#ax2.grid(False)


ax1.plot(vernier,sensor,lw=0.7,color='darkorange',label=r'Calibraci\'on 1 (cuadrado)')
ax1.plot(vernier_bis,1.2*sensor_bis,lw=0.7,color='steelblue',label=r'Calibraci\'on bis (cuadrado)')

#legend = plt.legend(loc='upper right',prop={'size':3})


#ax1.set_ylim(0, 0.025)
#ax1.set_yticks(np.arange(-200,-40,40))
#ax1.set_xlim(0, 2.5)
#ax1.set_xticks(np.arange(0,4,1))
#ax1.set_xlabel(r'$1/T$~(MeV$^{-1}$)')
#ax2.set_ylabel(r'$E_\mathrm{sym}$~(MeV)')
ax1.set_xlabel(r'Vernier~(V)')
ax1.set_ylabel(r'Sensor~(V)')
#ax2.set_ylabel(r'$\kappa$~(c/fm$^2$) (Nandi)')
#ax1.set_title(r'$\kappa$ for NSM ($\rho=0.05$, $x=0.5$ and $N=4.000$)')


pylab.savefig('fig2_version0.eps', format='eps', dpi=300, bbox_inches='tight')



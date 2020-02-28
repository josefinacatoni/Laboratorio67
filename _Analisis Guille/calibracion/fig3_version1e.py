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



def sliding_median(data_array, window):
#    data_array = array(data_array)
    new_list = []
    for i in range(len(data_array)):
        indices = range(max(i - window + 1, 0),
                        min(i + window + 1, len(data_array)))

        med = np.median([data_array[j] for j in indices])
        new_list.append(med)

    return new_list


#################### DATA LAMMPS ##############################

data1= np.genfromtxt('./fig3_version1a.dat', delimiter = '\t')	
data2= np.genfromtxt('./fig3_version1b.dat', delimiter = '\t')	
data3= np.genfromtxt('./fig3_version1c.dat', delimiter = '\t')	
data4= np.genfromtxt('./fig3_version1d.dat', delimiter = '\t')	

#################### PLOT specification ##############################


tiempo_a=data1[:,0]
vernier_a=data1[:,1]/np.amax(data1[:,1])
sensor_a=data1[:,2]/np.amax(data1[:,2])

tiempo_b=data2[:,0]
vernier_b=data2[:,1]/np.amax(data2[:,1])
sensor_b=data2[:,2]/np.amax(data2[:,2])

tiempo_c=data3[:,0]
vernier_c=data3[:,1]/np.amax(data3[:,1])
sensor_c=data3[:,2]/np.amax(data3[:,2])

tiempo_d=data4[:,0]
vernier_d=data4[:,1]/np.amax(data4[:,1])
sensor_d=data4[:,2]/np.amax(data4[:,2])


#################### DATA MANAGEMENT ##############################



#################### PLOT specification ##############################

fig=plt.figure(1)                # the first figure

ax1 = fig.add_subplot(111)

#ax1.grid(color='gray', linestyle='--', linewidth=0.3,axis='both')
ax1.grid(False)

ax1.plot(vernier_a,sensor_a,lw=0.4,color='olive',label=r'(a)')
ax1.plot(vernier_b,sensor_b,lw=0.4,color='steelblue',label=r'(b)')
ax1.plot(vernier_c,sensor_c,lw=0.4,color='firebrick',label=r'(c)')
ax1.plot(vernier_d,sensor_d,lw=0.4,color='orange',label=r'(d)')

legend = plt.legend(loc='lower right',prop={'size':3.5})

ax1.set_ylim(0, 1.0)
#ax1.set_yticks(np.arange(-200,-40,40))
ax1.set_xlim(0, 1.0)
#ax1.set_xticks(np.arange(0,4,1))
#ax1.set_xlabel(r'$1/T$~(MeV$^{-1}$)')
#ax2.set_ylabel(r'$E_\mathrm{sym}$~(MeV)')
ax1.set_xlabel(r'Vernier/V$_\mathrm{max}$')
ax1.set_ylabel(r'Sensor/S$_\mathrm{max}$')
#ax2.set_ylabel(r'$\kappa$~(c/fm$^2$) (Nandi)')
#ax1.set_title(r'Cuadrado bis')

pylab.savefig('fig3_version1e.eps', format='eps', dpi=300, bbox_inches='tight')

np.savetxt('fig3_version1e_normalized_a.dat', np.transpose([tiempo_a,vernier_a,sensor_a]), delimiter='\t', newline='\n')
np.savetxt('fig3_version1e_normalized_b.dat', np.transpose([tiempo_b,vernier_b,sensor_b]), delimiter='\t', newline='\n')
np.savetxt('fig3_version1e_normalized_c.dat', np.transpose([tiempo_c,vernier_c,sensor_c]), delimiter='\t', newline='\n')
np.savetxt('fig3_version1e_normalized_d.dat', np.transpose([tiempo_d,vernier_d,sensor_d]), delimiter='\t', newline='\n')





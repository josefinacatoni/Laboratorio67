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

data1= np.genfromtxt('./histo_1.dat', delimiter = '\t')	
data2= np.genfromtxt('./histo_2.dat', delimiter = '\t')	
data3= np.genfromtxt('./histo_3.dat', delimiter = '\t')	
data4= np.genfromtxt('./histo_4.dat', delimiter = '\t')	

#################### PLOT specification ##############################

steps1=data1[:,0]
histo1=data1[:,1]
steps2=data2[:,0]
histo2=data2[:,1]
steps3=data3[:,0]
histo3=data3[:,1]
steps4=data4[:,0]
histo4=data4[:,1]

histo1_smooth=sliding_median(data1[:,1],10)
histo2_smooth=sliding_median(data2[:,1],10)
histo3_smooth=sliding_median(data3[:,1],10)
histo4_smooth=sliding_median(data4[:,1],10)

#################### PLOT specification ##############################

fig=plt.figure(1)                # the first figure

ax1 = fig.add_subplot(111)

#ax1.grid(color='gray', linestyle='--', linewidth=0.3,axis='both')
ax1.grid(False)

ax1.loglog(steps1,histo1_smooth,lw=0.7,color='olive',zorder=1,label=r'sensor 1')
ax1.loglog(steps2,histo2_smooth,lw=0.7,color='orange',zorder=1,label=r'sensor 2')
ax1.loglog(steps3,histo3_smooth,lw=0.7,color='steelblue',zorder=1,label=r'sensor 3')

legend = plt.legend(loc='upper right',prop={'size':5})
#ax1.set_ylim(0, 0.005)
ax1.set_xlabel(r'levels')
ax1.set_ylabel(r'$P$')
ax1.set_title(r'Sensores')


pylab.savefig('fig_histo_4_version0.eps', format='eps', dpi=300, bbox_inches='tight')



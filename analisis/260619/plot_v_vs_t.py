'''
Este script grafica series temporales

Source de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html
'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
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

### DATA ###

data = np.genfromtxt('26062019_tarde.txt', delimiter = '\t')
time = np.linspace(0,len(data[:,0]),len(data[:,0])) 
sensor_1 = data[:,1] 
sensor_2 = data[:,2] 
sensor_3 = data[:,3] 
sensor_4 = data[:,4]

###  PLOT  ###

### Sensor 1 ###
plt.plot(time,sensor_1,color='green',linewidth='0.5',label='sensor 1') 

### Sensor 2 ###
plt.plot(time,sensor_2,color='orange',linewidth='0.5',label='sensor 2') 

### Sensor 3 ###
plt.plot(time,sensor_3,color='blue',linewidth='0.5',label='sensor 3') 

### Sensor 4 ###
#plt.plot(time,sensor_4,color='sienna',linewidth='0.5',label='sensor 4') 

pylab.grid(False)
pylab.xlabel('time')
pylab.ylabel('tension~(mV)')
pylab.ylim(0, 1000)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

pylab.savefig('v_vs_t_sensor_2606_tarde_p.png', format='png', dpi=300, bbox_inches='tight')
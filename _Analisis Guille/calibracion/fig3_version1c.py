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
          'axes.titlesize': 12,
          'axes.labelsize': 9,
          'legend.numpoints': 1,            # the number of points in the legend line
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 3,
          'ytick.labelsize': 3,
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

data1= np.genfromtxt('./cuadradoS13.dat', delimiter = '\t')	
data2= np.genfromtxt('./cuadradoS13bis_c.dat', delimiter = '\t')	

#################### PLOT specification ##############################


tiempo=data1[:,0]
vernier=data1[:,1]
sensor=data1[:,2]

tiempo_bis=data2[:,0]
vernier_bis=data2[:,1]
sensor_bis=data2[:,2]

vernier_min=np.amin(vernier)
vernier_bis_min=np.amin(vernier_bis)


sensor_min=np.amin(sensor)
sensor_bis_min=np.amin(sensor_bis)

#################### DATA MANAGEMENT ##############################

vernier_min=2.58
theta_one=1

n_bis=len(data2[:,0])

theta_bis=np.linspace(theta_one,theta_one,n_bis)
indice_bis=np.linspace(0,0,n_bis)
ruido_bis=np.linspace(0,0,n_bis)
indice_ruido_bis=np.linspace(0,0,n_bis)
sensor_bis_delta=np.linspace(0,0,n_bis)


i=1
theta_bis[0]=0

while i<n_bis:
	if vernier_bis[i]<vernier_min: theta_bis[i]=0
	i=i+1

i=1
j=1
indice_bis[0]=0

while i<n_bis:
	if theta_bis[i]>theta_bis[i-1]: j=j+1
	indice_bis[i]=j
	if theta_bis[i]==0: indice_bis[i]=0
	i=i+1

i=0
h=0

while i<n_bis:
	indice_ruido_bis[i]=h
	if theta_bis[i]==0: 
		ruido_bis[h]=sensor_bis[i]
		h=h+1
	i=i+1

ruido_bis_smooth=np.asarray(sliding_median(ruido_bis[0:h],10))

i=0

while i<n_bis:
	h=int(indice_ruido_bis[i])-1
        sensor_bis_delta[i]=sensor_bis[i]-ruido_bis_smooth[h]
	i=i+1

#mydata1=np.array(sorted(data1[19::20,2:4],key=getKey))


#################### PLOT specification ##############################

fig=plt.figure(1)                # the first figure

ax1 = fig.add_subplot(111)

#ax1.grid(color='gray', linestyle='--', linewidth=0.3,axis='both')
ax1.grid(False)

#ax2 = ax1.twinx()



#ax1.plot(tiempo_bis,0.05*indice_bis,lw=0.1,color='gray',linestyle='-',label=r'$\theta(v-v_\mathrm{min})$ ($v_\mathrm{min}=2.58$)')

#ax1.plot(tiempo_bis,2.5*(vernier_bis-vernier_bis_min)*theta_bis,lw=0.3,color='firebrick',label=r'Vernier')
#ax1.plot(tiempo_bis,sensor_bis_delta,lw=0.3,color='darkorange',label=r'Sensor')


#ax1.plot(tiempo_bis,(vernier_bis-vernier_bis_min)*theta_bis,lw=0.3,color='firebrick',label=r'Vernier sin el offset')
#ax1.plot(tiempo_bis,sensor_bis_delta,lw=0.3,color='darkorange',label=r'Sensor sin el offset')

ax1.plot((vernier_bis-vernier_bis_min)*theta_bis,sensor_bis_delta,lw=0.3,color='firebrick',label=r'Vernier sin el offset')


#legend = plt.legend(loc='upper left',prop={'size':2.5})


#ax1.set_ylim(0, 0.025)
#ax1.set_yticks(np.arange(-200,-40,40))
#ax1.set_xlim(0, 2.5)
#ax1.set_xticks(np.arange(0,4,1))
#ax1.set_xlabel(r'$1/T$~(MeV$^{-1}$)')
#ax2.set_ylabel(r'$E_\mathrm{sym}$~(MeV)')
#ax1.set_xlabel(r'tiempo~(seg.)')
#ax1.set_ylabel(r'Voltaje~(V)')
#ax2.set_ylabel(r'$\kappa$~(c/fm$^2$) (Nandi)')
#ax1.set_title(r'Cuadrado bis')


pylab.savefig('fig3_version1c.eps', format='eps', dpi=300, bbox_inches='tight')

np.savetxt('fig3_version1c.dat', np.transpose([tiempo_bis,(vernier_bis-vernier_bis_min)*theta_bis,sensor_bis_delta]), delimiter='\t', newline='\n')





"""
Solving the advection equation using FTCS and Lax-Freidrich methods,
and simulating the solutions.

Created on Wednesday Feb 25 7:20 pm

@author: Juliann Wray
"""
import numpy as np
import matplotlib.pyplot as plt



# We use the following advection parameters for the flow: 
n = 50
dt = 1
dx = 1

 #With the step for velocity = -0.1 (given value)
s = -0.1*dt/2/dx

#Position x (cartesian system) for the advection equation:
x = np.arange(n)*dx

#ion() creates the animation
plt.ion()
fig, axes = plt.subplots(nrows=1, ncols=2)

#---------------Forward time central space method plots:-------------------------------

#Define the function for FTCS
f_Ftcs = np.array(x)*1./n 

#Title the subplot
axes[0].set_title('Advection FTCS')

#As shown in class, show the intial state on the plot
axes[0].plot(x, f_Ftcs, 'bp')

#Make the plot! This is looped through below
pltFTCS, = axes[0].plot(x, f_Ftcs, 'bp')

#-------------- Lax-Friedrichs Method plots: ---------------------------------
#Define the function for LF
f_Lf = np.array(x)*1./n 

#Title the subplot
axes[1].set_title('Advection - LF')

#As shown in class, show the intial state on the plot
axes[1].plot(x, f_Lf, 'gp')

#Make the plot that will be looped through below.
pltLF, = axes[1].plot(x, f_Lf, 'gp')

#Aligning the axes 
for ax in axes:
    ax.set_xlim([0, n])
    ax.set_ylim([0,2])
    
fig.canvas.draw()

#This evolution below is entirely based on the code shown in class.
# Loop through the functions to update the state of the systems
count =0
Nsteps = 5000
while count < Nsteps:
    
    # FTCS
    f_Ftcs[1:n-1] = f_Ftcs[1:n-1] - s*(f_Ftcs[2:] - f_Ftcs[:n-2])
    
    # Lax-Friedrich
    f_Lf[1:n-1] = 0.5*(f_Lf[2:] + f_Lf[:n-2]) - s*(f_Lf[2:] - f_Lf[:n-2])
    
    # update the plot
    pltFTCS.set_ydata(f_Ftcs)
    pltLF.set_ydata(f_Lf)
    
    fig.canvas.draw()
    plt.pause(0.001)
    count += 1


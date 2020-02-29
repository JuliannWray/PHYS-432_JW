# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:06:22 2020

@author: jemwr
"""

import numpy as np
import matplotlib.pyplot as plt



# We initialize following parameters for the flow:
dt = 1 
n=50
dx = 1

#a & b are constants, where a = D*dt/dx**2 with D = 1 and b = v*dt/dx with
#v = 0.01, given in the question.
a = -0.01*dt/dx

b = 1*dt/dx**2


#----------------------Lax_Freidrich advection
#Initialize the array for position x and  values in a cartesian system
x = np.arange(n)*dx
f_LF = np.full(n,1)
f_Im = np.full(n,1)


# ion() creates the animation. We want 2 subplots
plt.ion()
fig, axes = plt.subplots(nrows=1, ncols=2)
#---------------------LF method plots: ------------------------------


#Title the subplot
axes[0].set_title('Advection (LF)')

#As shown in class, show the intial state on the plot
axes[0].plot(x,f_LF, 'bp')

#Make the plot! This is looped through below
pltLF, = axes[0].plot(x, f_LF, 'bp')



#-----------------Implicit method plots:---------------------------
#Title the subplot
axes[1].set_title('Diffusion (Implicit)')

#As shown in class, show the intial state on the plot
axes[1].plot(x,f_Im, 'bp')

#Make the plot! This is looped through below
pltIm, = axes[1].plot(x, f_Im, 'bp')

fig.canvas.draw()


Nsteps = 1000 
count = 0
while count < Nsteps:
	
    #Lax Freidrich
    f_LF[-1] = 1.0 #boudary conditions
    f_LF[0] = 0.0
    
    
    f_LF[1:n - 1] = (0.5 *(f_LF[:n-2] + f_LF[2:]) - 0.5*a*(-f_LF[:n-2] + f_LF[2:]))
   
     
    # implicit
    f_Im[-1] = 1.0 #boundary conditions
    f_Im[0] = 0.0
    
    A = np.eye(n) * (1 + 2 * b) + (-b) * np.eye(n, k=1) + (-b) * np.eye(n, k=-1)

    #upper bounds
    A[n-1][n-1] = 1.0
    A[n-1][n-2] = 0.0
    #lower bounds 
    A[0][0] = 1.0
    A[0][1] = 0.0		
    f_Im = np.linalg.solve(A,f_Im)
    
        
		
    # update the plot
    pltLF.set_ydata(f_LF)
    pltIm.set_ydata(f_Im)
    fig.canvas.draw()
    plt.pause(0.01)
    count +=1
	


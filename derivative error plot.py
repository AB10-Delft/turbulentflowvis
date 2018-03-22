import numpy as np
from math import *
import matplotlib.pyplot as plt
import pylab


def backward(x,h):
    result= (sin(x)-sin(x-h))/(h)
    return result       

def forward(x,h):
    result = (sin(x+h)-sin(x))/(h)
    return result

def central(x,h):
    result = (sin(x+h)-sin(x-h))/(2*h)
    return result

k = 10000
N = []
back_error = []
forw_error = []
centr_error = []

for n in range(100,k,100):
    back = []
    forw = []
    centr = []
    C = []
    h = 2*pi/float(n-1)
    n = float(n)
    for x in np.linspace(0,2*pi,n):
        
        b = backward(x,h)
        
        f = forward(x,h)
        
        c=central(x,h)
        
        forw.append(f)
        back.append(b)
        centr.append(c)
        C.append(cos(x))
    
    back_err = []    
    forw_err = []
    centr_err = []
    
    
    for i in  range(len(back)):
        y = abs(back[i]-C[i]) 
        z = abs(forw[i]-C[i])
        w = abs(centr[i]-C[i])
        
        back_err.append(y)
        forw_err.append(z)
        centr_err.append(w)
        
        
        
    
    N.append(n)
    back_error.append(sum(back_err)/len(back_err))
    forw_error.append(sum(forw_err)/len(forw_err))
    centr_error.append(sum(centr_err)/len(centr_err))
    

for i in range(len(N)):
    N[i] = log(N[i],10)
    back_error[i] = log(back_error[i],10)
    forw_error[i] = log(forw_error[i],10)
    centr_error[i] = log(centr_error[i],10)

#print len(N), len(error)

back_slope = (N[60]-N[59])/(back_error[60]-back_error[59])
print "Backward Difference Scheme Slope =", back_slope

forw_slope = (N[80]-N[79])/(forw_error[80]-forw_error[79])
print "Forward Difference Scheme Slope =",  forw_slope

centr_slope = (N[80]-N[79])/(centr_error[80]-centr_error[79])
print "Central Difference Scheme Slope = ", centr_slope



plt.plot(N,back_error,label='Backward Difference Scheme')
plt.plot(N,forw_error,label='Forward Difference Scheme')
plt.plot(N,centr_error,label='Central Difference Scheme')

plt.xlabel('Evaluation steps (log)')
plt.ylabel('Error (log)')
plt.title('Error Decay of Differentiation Schemes')
plt.legend()
    
plt.show()


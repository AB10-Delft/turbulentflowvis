import numpy as np
from math import *
import matplotlib.pyplot as plt
import pylab
from scipy import stats

plt.rcParams['axes.facecolor'] = 'white'


def backward(x,h):
    result= (sin(x)-sin(x-h))/(h)
    return result       

def forward(x,h):
    result = (sin(x+h)-sin(x))/(h)
    return result

def central(x,h):
    result = (sin(x+h)-sin(x-h))/(2*h)
    return result
    
def highorder(x,h):
    result = (-sin(x+2*h)+8*sin(x+h)-8*sin(x-h)+sin(x-2*h))/(12*h)
    return result
    
k = 10000
N = []
back_error = []
forw_error = []
centr_error = []
high_error = []


for n in range(100,k,100):
    back = []
    forw = []
    centr = []
    high = []
    
    C = []
    h = 2*pi/float(n-1)
    n = float(n)
    for x in np.linspace(0,2*pi,n):
        
        b = backward (x,h)
        
        f = forward (x,h)
        
        c = central (x,h)
        
        o = highorder (x,h)
        
        forw.append(f)
        back.append(b)
        centr.append(c)
        high.append(o)
        C.append(cos(x))
    
    back_err = []    
    forw_err = []
    centr_err = []
    high_err=[]
    
    
    for i in  range(len(back)):
        y = abs(back[i]-C[i]) 
        z = abs(forw[i]-C[i])
        w = abs(centr[i]-C[i])
        x = abs(high[i]-C[i])
        
        back_err.append(y)
        forw_err.append(z)
        centr_err.append(w)
        high_err.append(x)
        
        
        
    
    N.append(n)
    back_error.append(sum(back_err)/len(back_err))
    forw_error.append(sum(forw_err)/len(forw_err))
    centr_error.append(sum(centr_err)/len(centr_err))
    high_error.append(sum(high_err)/len(high_err))
  

    

for i in range(len(N)):
    N[i] = log(N[i],10)
    back_error[i] = log(back_error[i],10)
    forw_error[i] = log(forw_error[i],10)
    high_error[i] = log(high_error[i],10)
    centr_error[i] = log(centr_error[i],10)


slopeh, intercepth, r_value, p_value, std_err = stats.linregress (N, high_error)
slopef, interceptf, r_value, p_value, std_err = stats.linregress (N, forw_error)
slopeb, interceptb, r_value, p_value, std_err = stats.linregress (N, back_error)
slopec, interceptc, r_value, p_value, std_err = stats.linregress (N, centr_error)

fit1 = []
fit2 = []
fit3 = []
fit4 = []
for i in range(len(N)):
    fit1.append(intercepth + slopeh*N[i])
    fit2.append(interceptf + slopef*N[i])
    fit3.append(interceptb + slopeb*N[i])
    fit4.append(interceptc + slopec*N[i])
    
print 'High Order Slope: ', slopeh
print 'Forward Order Slope: ', slopef
print 'Backword Order Slope: ', slopeb
print 'Central Order Slope: ', slopec


plt.plot(N, fit1,  label='Fitted line High Order')
plt.plot(N, fit2,  label='Fitted line Forward')
plt.plot(N, fit3,  label='Fitted line Backward')
plt.plot(N, fit4,  label='Fitted line Central')
 

plt.plot(N,back_error, 'o', label='Original Data Backward Difference Scheme')
plt.plot(N,forw_error, 'o', label='Origina Data Forward Difference Scheme')
plt.plot(N,centr_error,'o', label='Original Data Central Difference Scheme')
plt.plot(N,high_error,'o', label='Original Data High Order ')


plt.xlabel('Evaluation steps (log)')
plt.ylabel('Error (log)')
plt.title('Error Decay of Differentiation Schemes')
plt.legend()
    
plt.show()


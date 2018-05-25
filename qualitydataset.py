## Imports
import numpy as np
import scipy.io as sc
import scipy
import timeit
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import simps
from numpy import trapz
from matplotlib.patches import Polygon

## Read the data
def read_data(name,DIM):
    """ Reads .mat files into numpy arrays """
    dt = sc.loadmat(name +'.mat')
    vel_u =  dt['u']
    vel_w =  dt['w']
    vel_v = dt['v']
    U = np.empty(vel_u.shape + (DIM,))
    U[...,0] = vel_u
    U[...,1] = vel_v
    U[...,2] = vel_w

    return vel_u,vel_v,vel_w,U
vel_u, vel_v, vel_w, U = read_data('data_001',3) # 256,256,768
x,y,z = 256,256,768

##----------------------------------------------------------------------------------------------------------------------##

## Mean calculation
meanu, meanv, meanw = np.mean(vel_u), np.mean(vel_v), np.mean(vel_w)
print 'mean values',meanu, meanv, meanw

##----------------------------------------------------------------------------------------------------------------------##

## Variance calculation
varu, varv, varw = np.var(vel_u, ddof = 1), np.var(vel_v,ddof = 1), np.var(vel_w,ddof = 1)
print 'variances',varu, varv, varw

##----------------------------------------------------------------------------------------------------------------------##

## Two point correlation calculation
def twopointcorrelation(vel):
    C = np.correlate(vel,vel,'full')
    C = C[len(vel)-1:] # you can skip the negative part of the correlate function, thus the first half is not necessary
    return C

# for x
Xcorrelation = x*[0]
for j in range(y):
    for k in range(z):
        phi = vel_u[:,j,k] # define a point in mesh
        a = twopointcorrelation(phi) # use function to find the two point correlation there
        Xcorrelation = Xcorrelation + a # add the two point correlation, later divide by amount of points to find the average

Xcorrelation = Xcorrelation/y/z # find average of the correlations
Xcorrelation = Xcorrelation/Xcorrelation[0] # normalize values

xtab = np.linspace(0,2*pi,x)

Xcorrelation1 = Xcorrelation[:len(Xcorrelation)/2] # only need to integrate first half
xtab1 = xtab[:len(xtab)/2] # xtab for first half

Xarea = scipy.integrate.simps(Xcorrelation1,xtab1) # find area under curve of the first half of the average correlation

# for y
Ycorrelation = y*[0]
for i in range(x):
    for k in range(z):
        phi = vel_v[i,:,k] # define a point in mesh
        a = twopointcorrelation(phi) # use function to find the two point correlation there
        Ycorrelation = Ycorrelation + a # add the two point correlation, later divide by amount of points to find the average

Ycorrelation = Ycorrelation/x/z # find average of the correlations
Ycorrelation = Ycorrelation/Ycorrelation[0] # normalize values

ytab = np.linspace(0,2*pi,y)

Ycorrelation1 = Ycorrelation[:len(Ycorrelation)/2] # only need to integrate first half
ytab1 = ytab[:len(ytab)/2] # xtab for first half

Yarea = scipy.integrate.simps(Ycorrelation1,ytab1) # find area under curve of the first half of the average correlation

# for z
Zcorrelation = z*[0]
for i in range(x):
    for j in range(y):
        phi = vel_w[i,j,:] # define a point in mesh
        a = twopointcorrelation(phi) # use function to find the two point correlation there
        Zcorrelation = Zcorrelation + a # add the two point correlation, later divide by amount of points to find the average

Zcorrelation = Zcorrelation/x/y # find average of the correlations
Zcorrelation = Zcorrelation/Zcorrelation[0] # normalize values

ztab = np.linspace(0,2*pi,z)

Zcorrelation1 = Zcorrelation[:len(Zcorrelation)/2] # only need to integrate first half
ztab1 = ztab[:len(ztab)/2] # xtab for first half

Zarea = scipy.integrate.simps(Zcorrelation1,ztab1) # find area under curve of the first half of the average correlation

print 'areas',Xarea,Yarea,Zarea
print '2*pi/area',2*pi/Xarea,2*pi/Yarea,2*pi/Zarea

plt.subplot(3,1,1)
plt.title("Normalized correlation vel u in x-direction")
plt.plot(xtab,Xcorrelation)
plt.subplot(3,1,2)
plt.title("Normalized correlation vel v in y-direction")
plt.plot(ytab,Ycorrelation)
plt.subplot(3,1,3)
plt.title("Normalized correlation vel w in z-direction")
plt.plot(ztab,Zcorrelation)
plt.show()

plt.figure(figsize=(12,16),dpi=200)
#plt.title('Normalized two point correlation in three directions')
plt.plot(xtab,Xcorrelation,color='r')
plt.plot(ytab,Ycorrelation)
plt.plot(ztab,Zcorrelation)
plt.legend(['u in x-direction',"v in y-direction",'w in z-direction'],loc='upper right',prop={'size':8})
plt.ylabel("Normalized two point correlation")
plt.xlabel("Distance along axis")
plt.grid(True)
plt.show()

# # Test correlate function
# Ctest = []
# for k in range(len(phi)):
#     sum = 0
#     x = len(phi) - k - 1
#     for n in range(len(phi)):
#         if n > x:
#             break
#         sum = sum + phi[n+k]*phi[n]
#     Ctest.append(sum)
# #print Ctest, len(Ctest)

# Test notation
# print vel_u[:,1,2]
# print vel_u

# A = np.reshape(np.arange(1,28),(3,3,3))
# print A
# print A[:,1,2]

import numpy as np
import scipy.io as sc
import timeit
from tvtk.api import tvtk, write_data
from math import *

DIM = 3

####  read the matlabfile
start = timeit.default_timer()
print 'Reading...',
dt = sc.loadmat('raw_data_1.mat')
print timeit.default_timer() - start, 's'


### using correct keys, obtain three 3D matrixes, representing u,v,w velocities (scalar fields)
vel_u =  dt['u']
vel_w =  dt['w']
vel_v = dt['v']
U = np.empty(vel_u.shape + (DIM,))  #.shape returns tuple so, a tupple (x,) must be added
                                    # 3 times (192,192,192) cubes
U[...,0] = vel_u #equivalent to U[:,:,:,0], reduces the dimension by one
U[...,1] = vel_v
U[...,2] = vel_w


### specify the dimension (192 for this case)
ushape = np.array(U.shape[:-1]) #converts from tuple to array
#print U.shape[:-1]  #4 entries, (192,192,192,3)
n = U.shape[0]

def jac_vec(Uin, h):
    out = np.zeros(tuple(ushape-4) + (DIM,DIM)) #  (188,188,188,3,3)
    U = Uin[:,2:-2,2:-2,:]  # view array wihtout j,k halo  (cut off j,k sides to 188 to work with i)
    out[...,0,:] = (-U[4:,:,:] + 8*U[3:-1,:,:] - 8*U[1:-3,:,:] + U[:-4,:,:])/(12.*h) #(4 used to account for 192 -> 188)
    U = Uin[2:-2,:,2:-2,:]  # view array wihtout i,k halo
    out[...,1,:] = (-U[:,4:,:] + 8*U[:,3:-1,:] - 8*U[:,1:-3,:] + U[:,:-4,:])/(12.*h)
    U = Uin[2:-2,2:-2,:,:]  # view array wihtout i,j halo
    out[...,2,:] = (-U[:,:,4:] + 8*U[:,:,3:-1] - 8*U[:,:,1:-3] + U[:,:,:-4])/(12.*h)
    return out


def q_vec(J):  #(i,j,k,velocity,direction)
    return J[...,0,0]*J[...,1,1]-J[...,0,1]*J[...,1,0]+J[...,0,0]*J[...,2,2]-J[...,0,2]*J[...,2,0]+J[...,1,1]*J[...,2,2]-J[...,1,2]*J[...,2,1]
    
## set the h to divide by:
h = pi/(n-1)

## start timer, run the main loop and fill the Q matrix

start = timeit.default_timer()
print 'Vectorized...',
jac1 = jac_vec(U, h)
q1 = q_vec(jac1)
#print q1.shape
print timeit.default_timer() - start, 's'

print q1[0,0,0]


### write the 3D array into vtk

#grid = tvtk.ImageData(spacing=(188,188,188), origin=(0,0,0),dimensions=flow_Q.shape)
#grid.point_data.scalars = np.ravel(flow_Q,order = 'F')
#grid.point_data.scalars.name = 'Test Data'
#write_data(grid, 'test.vtk')              

                 


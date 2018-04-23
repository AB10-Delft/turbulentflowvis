import numpy as np
import scipy.io as sc
from jacobian_4 import jac4
import timeit



####  read the matlabfile
dt = sc.loadmat('raw_data_1.mat')

### using correct keys, obtain three 3D matrixes, representing u,v,w velocities (scalar fields)
vel_u =  dt['u']
vel_w =  dt['w']
vel_v = dt['v']


### transform the matrixes into arrays, because arrays are "better"
vel_u = np.squeeze(np.asarray(vel_u))
vel_w = np.squeeze(np.asarray(vel_w))
vel_v = np.squeeze(np.asarray(vel_v))




### Evaluate Jacobian at each point, and calculate Q

## define Q
def Q(mtx):
    return (mtx[0,0]*mtx[1,1]-mtx[0,1]*mtx[1,0])+(mtx[0,0]*mtx[2,2]-mtx[0,2]*mtx[2,0])+(mtx[1,1]*mtx[2,2]-mtx[1,2]*mtx[2,1])

## Define constants
flow = np.zeros((188,188,188))
r = range(2,189)
h = 1.

## start timer
start = timeit.default_timer()

for i in r:
    for j in r:
        for k in r:
            flow[i,j,k] = Q(jac4(vel_u,vel_v,vel_w,i,j,k,h))
                 
stop = timeit.default_timer()
print "ready"
print "time elapsed: ", stop - start, "s"
print flow.shape

### clean memory

vel_u = 0
vel_v = 0
vel_w = 0


grid = tvtk.ImageData(spacing=(10, 5, -10), origin=(100, 350, 200), 
                      dimensions=flow.shape)
grid.point_data.scalars = np.ravel(flow,order = 'F')
grid.point_data.scalars.name = 'Test Data'
#write_data(grid, 'test.vtk')
import numpy as np
import scipy.io as sc
from jacobian_file import jacobian_point
import timeit
from enthought.mayavi import mlab
from enthought.tvtk.api import tvtk, write_data


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



### combine all arrays

C = np.zeros((192,192,192),dtype = 'object')

for i in range(192):
    for j in range(192):
        for k in range(192):
            C[i,j,k] = [vel_u[i,j,k],vel_v[i,j,k],vel_w[i,j,k]]
    

### Evaluate Jacobian at each point, and calculate Q

def Q(mtx):
    return (mtx[0,0]*mtx[1,1]-mtx[0,1]*mtx[1,0])+(mtx[0,0]*mtx[2,2]-mtx[0,2]*mtx[2,0])+(mtx[1,1]*mtx[2,2]-mtx[1,2]*mtx[2,1])

flow = np.zeros((192,192,192))
r = range(0,192)

start = timeit.default_timer()

for i in r:
    for j in r:
        for k in r:
            flow[i,j,k] = Q(jacobian_point(C,i,j,k))
                 
stop = timeit.default_timer()
print "ready"
print "time elapsed: ", stop - start, "s"
print flow.shape

### clean memory

C = 0
vel_u = 0
vel_v = 0
vel_w = 0

#to plot
#src = mlab.pipeline.scalar_field(flow[::8][::1][::1])
#mlab.pipeline.iso_surface(src, contours=100)
#mlab.outline()
#mlab.show()

grid = tvtk.ImageData(spacing=(10, 5, -10), origin=(100, 350, 200), 
                      dimensions=flow.shape)
grid.point_data.scalars = np.ravel(flow,order = 'F')
grid.point_data.scalars.name = 'Test Data'
#write_data(grid, 'test.vtk')



import numpy as np
from Q_clean import *
import timeit

def save(data1,qq):
    """ lamda2, 'name of file'"""

    #create the grid and create first data set
    grid = tvtk.ImageData(spacing=data1.shape, origin=(0,0,0),dimensions=data1.shape)
    grid.point_data.scalars = np.ravel(data1,order = 'F')
    grid.point_data.scalars.name = 'lamda2'

    #write the data
    write_data(grid, qq+ '.vtk')



start = timeit.default_timer()
print "Reading...",
u,v,w,U = read_data('validation_Q_l2',3)
print timeit.default_timer() - start, 's'

start = timeit.default_timer()
print "Calculating...",
J = jac_vec(U)
J_t = np.transpose(J,(0,1,2,4,3))
S = (J_t + J)/2.
O = (J_t - J)/2.
L = np.matmul(S,S) + np.matmul(O,O)
eigen = np.empty((92,92,92,3))
eigen = np.linalg.eigvals(L)
eigen.sort()   #it seems that sorting is element wise
l2 = eigen[...,1]   
print timeit.default_timer() - start, 's'

##start = timeit.default_timer()
##print "Looping...",
##check = np.empty((92,92,92))
##r = range(0,92)
##for i in r:
##    for j in r:
##        for k in r:
##            check[i,j,k] = np.linalg.eigvals(L[i,j,k,...])[1]

start = timeit.default_timer()
print "Writing...",
import warnings as w
w.simplefilter(action = 'ignore', category = FutureWarning)
save(l2,"lambda2_vector_v2")
w.resetwarnings()
print timeit.default_timer() - start, 's'


##start = timeit.default_timer()
##r = range(0,188)
##check = np.empty((188,188,188))
##for i in r:
##    for j in r:
##        for k in r:
##            check[i,j,k] = np.linalg.eigvals(L[i,j,k,...])[1]
##print timeit.default_timer() - start, 's'
            

import numpy as np
import scipy.io as sc
import timeit
from math import *
from tvtk.api import tvtk, write_data

#define all stand alone functions

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

def jac_vec(Uin):
    """ Returns jacobian vector for the entire matrix """
    n = np.array(Uin.shape)[0]
    ushape = np.array(Uin.shape[:-1])
    DIM = np.array(Uin.shape)[-1:][0]
    h = pi/(n-1)
    out = np.zeros(tuple(ushape-4) + (DIM,DIM))
    U = Uin[:,2:-2,2:-2,:]  # view array wihtout j,k halo
    out[...,0,:] = (-U[4:,:,:] + 8*U[3:-1,:,:] - 8*U[1:-3,:,:] + U[:-4,:,:])/(12.*h)
    U = Uin[2:-2,:,2:-2,:]  # view array wihtout i,k halo
    out[...,1,:] = (-U[:,4:,:] + 8*U[:,3:-1,:] - 8*U[:,1:-3,:] + U[:,:-4,:])/(12.*h)
    U = Uin[2:-2,2:-2,:,:]  # view array wihtout i,j halo
    out[...,2,:] = (-U[:,:,4:] + 8*U[:,:,3:-1] - 8*U[:,:,1:-3] + U[:,:,:-4])/(12.*h)
    return out

def q_vec(J):
    return J[...,0,0]*J[...,1,1]-J[...,0,1]*J[...,1,0]+J[...,0,0]*J[...,2,2]-J[...,0,2]*J[...,2,0]+J[...,1,1]*J[...,2,2]-J[...,1,2]*J[...,2,1]

def save(data1,qq):
    """ Q data, 'name of file'"""

    #create the grid and create first data set
    grid = tvtk.ImageData(spacing=data1.shape, origin=(0,0,0),dimensions=data1.shape)
    grid.point_data.scalars = np.ravel(data1,order = 'F')
    grid.point_data.scalars.name = 'Q method'

    #write the data
    write_data(grid, qq+ '.vtk')


def Q_method(name1,DIM,new_name):
    """ .mat file, dimension, .vtk file """
    
    #read
    start = timeit.default_timer()
    print 'Reading...',
    u,v,w,mtx = read_data(name1,DIM)
    print timeit.default_timer() - start, 's'
    
    #compute
    start = timeit.default_timer()
    print 'Computing...',
    Q = q_vec(jac_vec(mtx))
    print timeit.default_timer() - start, 's'
    
    #write
    start = timeit.default_timer()
    import warnings as w
    w.simplefilter(action = 'ignore', category = FutureWarning)
    print 'Writing...',
    save(Q,new_name)
    w.resetwarnings()
    print timeit.default_timer() - start, 's'
    
    
    

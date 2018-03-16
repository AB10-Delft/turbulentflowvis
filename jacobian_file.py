import scipy.io as sc
import numpy as np
import timeit

### This version uses predefined tools:


def central(mtx,i,j,k,comp, drct, step = 2.):
    """ matrix, position, component-'u','v','w', direction-'x','y','z'"""
    ## decide which component to iterate
    if comp == 'u':
        vel = 0
    elif comp == 'v':
        vel = 1
    else:            # reduces runtime
        vel = 2

    if drct == 'x':
        prim = (mtx[i+1,j,k][vel]-mtx[i-1,j,k][vel])/step
        return prim
    elif drct == 'y':
        prim = (mtx[i,j+1,k][vel]-mtx[i,j-1,k][vel])/step
        return prim
    else:                 # reduces runtime
        prim = (mtx[i,j,k+1][vel]-mtx[i,j,k-1][vel])/step
        return prim
    

def forward(mtx,i,j,k,comp, drct, step = 1.):
    """ matrix, position, component-'u','v','w', direction-'x','y','z'"""
    ## decide which component to iterate
    if comp == 'u':
        vel = 0
    elif comp == 'v':
        vel = 1
    else:            # reduces runtime
        vel = 2

    if drct == 'x':
        prim = (mtx[i+1,j,k][vel]-mtx[i,j,k][vel])/step
        return prim
    elif drct == 'y':
        prim = (mtx[i,j+1,k][vel]-mtx[i,j,k][vel])/step
        return prim
    else:                 # reduces runtime
        prim = (mtx[i,j,k+1][vel]-mtx[i,j,k][vel])/step
        return prim

    
    
def backward(mtx,i,j,k,comp, drct, step = 1.):
    """ matrix, position, component-'u','v','w', direction-'x','y','z'"""
    ## decide which component to iterate
    if comp == 'u':
        vel = 0
    elif comp == 'v':
        vel = 1
    else:            # reduces runtime
        vel = 2
    ## work with the direction
    if drct == 'x':
        prim = (mtx[i,j,k][vel]-mtx[i-1,j,k][vel])/step
        return prim
    elif drct == 'y':
        prim = (mtx[i,j,k][vel]-mtx[i,j-1,k][vel])/step
        return prim
    else:                 # reduces runtime
        prim = (mtx[i,j,k][vel]-mtx[i,j,k-1][vel])/step
        return prim

    
    
def jacobian_point(mtx,i,j,k):
    """ Returns the 3x3 for a given point"""
    velocities = ['u','v','w']
    directions = ['x','y','z']
    check = [i,j,k]
    temp = np.zeros((3,3))   #creates a 3x3 matrix for each point
    for n,drct in enumerate(directions):
        for m,comp in enumerate(velocities):
            if check[n] == 0:
                temp[n,m] = forward(mtx,i,j,k,comp,drct)
            elif check[n] == 191:
                temp[n,m] = backward(mtx,i,j,k,comp,drct)
            else:
                temp[n,m] = central(mtx,i,j,k,comp,drct)
    return temp




def jacobian(mtx):
    """ Returns 3x3 for all the matrix"""
    J = np.zeros((192,192,192),dtype='object')
    r = range(0,192)
    velocities = ['u','v','w']
    directions = ['x','y','z']
    for i in r:
        for j in r:
            for k in r:
                check = [i,j,k]
                temp = np.zeros((3,3))   #creates a 3x3 matrix for each point
                for n,drct in enumerate(directions):
                    for m,comp in enumerate(velocities):
                        if check[n] == 0:
                            temp[n,m] = forward(mtx,i,j,k,comp,drct)
                        elif check[n] == 191:
                            temp[n,m] = backward(mtx,i,j,k,comp,drct)
                        else:
                            temp[n,m] = central(mtx,i,j,k,comp,drct)
                J[i,j,k] = temp
                #print temp
    return J
    
    
    

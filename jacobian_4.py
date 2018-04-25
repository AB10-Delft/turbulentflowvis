import numpy as np

def prim_x(mtx,x,j,k,h):
    prim = (-mtx[x+2*h,j,k]+8*mtx[x+h,j,k]-8*mtx[x-h,j,k]+mtx[x-2*h,j,k])/(12*h)
    return prim

def prim_y(mtx,i,y,k,h):
    prim = (-mtx[i,y+2*h,k]+8*mtx[i,y+h,k]-8*mtx[i,y-h,k]+mtx[i,y-2*h,k])/(12*h)
    return prim

def prim_z(mtx,i,j,z,h):
    prim = (-mtx[i,j,z+2*h]+8*mtx[i,j,z+h]-8*mtx[i,j,z-h]+mtx[i,j,z-2*h])/(12*h)
    return prim

def jac4(vel_u,vel_v,vel_w,i,j,k,h):
    J = np.zeros((3,3))
    J[0,0] = prim_x(vel_u,i,j,k,h)
    J[0,1] = prim_x(vel_v,i,j,k,h)
    J[0,2] = prim_x(vel_w,i,j,k,h)

    J[1,0] = prim_y(vel_u,i,j,k,h)
    J[1,1] = prim_y(vel_v,i,j,k,h)
    J[1,2] = prim_y(vel_w,i,j,k,h)

    
    J[2,0] = prim_z(vel_u,i,j,k,h)
    J[2,1] = prim_z(vel_v,i,j,k,h)
    J[2,2] = prim_z(vel_w,i,j,k,h)

    return J

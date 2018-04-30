#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
from math import *

#def prim_x(mtx,x,j,k,h):
#    h_new = 2*pi/95
#    prim = (-mtx[x+2*h,j,k]+8*mtx[x+h,j,k]-8*mtx[x-h,j,k]+mtx[x-2*h,j,k])/(12*h_new)
#    return prim
#
#def prim_y(mtx,i,y,k,h):
#    h_new = 2*pi/95
#    prim = (-mtx[i,y+2*h,k]+8*mtx[i,y+h,k]-8*mtx[i,y-h,k]+mtx[i,y-2*h,k])/(12*h_new)
#    return prim
#
#def prim_z(mtx,i,j,z,h):
#    h_new = 2*pi/95
#    prim = (-mtx[i,j,z+2*h]+8*mtx[i,j,z+h]-8*mtx[i,j,z-h]+mtx[i,j,z-2*h])/(12*h_new)
#    return prim

def jac4(vel_u,vel_v,vel_w,i,j,k,h):
    J = np.zeros((3,3))
    h_new = 2*pi/191
    
    J[0,0] = (-vel_u[i+2*h,j,k]+8*vel_u[i+h,j,k]-8*vel_u[i-h,j,k]+vel_u[i-2*h,j,k])/(12*h_new)
    J[0,1] = (-vel_v[i+2*h,j,k]+8*vel_v[i+h,j,k]-8*vel_v[i-h,j,k]+vel_v[i-2*h,j,k])/(12*h_new)
    J[0,2] = (-vel_w[i+2*h,j,k]+8*vel_w[i+h,j,k]-8*vel_w[i-h,j,k]+vel_w[i-2*h,j,k])/(12*h_new)

    J[1,0] = (-vel_u[i,j+2*h,k]+8*vel_u[i,j+h,k]-8*vel_u[i,j-h,k]+vel_u[i,j-2*h,k])/(12*h_new)
    J[1,1] = (-vel_v[i,j+2*h,k]+8*vel_v[i,j+h,k]-8*vel_v[i,j-h,k]+vel_v[i,j-2*h,k])/(12*h_new)
    J[1,2] = (-vel_w[i,j+2*h,k]+8*vel_w[i,j+h,k]-8*vel_w[i,j-h,k]+vel_w[i,j-2*h,k])/(12*h_new)

    
    J[2,0] = (-vel_u[i,j,k+2*h]+8*vel_u[i,j,k+h]-8*vel_u[i,j,k-h]+vel_u[i,j,k-2*h])/(12*h_new)
    J[2,1] = (-vel_v[i,j,k+2*h]+8*vel_v[i,j,k+h]-8*vel_v[i,j,k-h]+vel_v[i,j,k-2*h])/(12*h_new)
    J[2,2] = (-vel_w[i,j,k+2*h]+8*vel_w[i,j,k+h]-8*vel_w[i,j,k-h]+vel_w[i,j,k-2*h])/(12*h_new)

    return J

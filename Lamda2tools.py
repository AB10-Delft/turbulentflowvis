#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
from scipy import linalg as lg
import time


def l2(jac):
    #t0 = time.time()
    jacT = jac.transpose()
    #S and Omega, the main parameters of the method
    S = (jacT + jac) / 2.
    O = (jacT - jac) / 2.
        
    #t1 = time.time()
    #print (t1-t0)*100000
    #Intermediate step, S^2 + O^2
    L = np.matmul(S,S) + np.matmul(O,O)
    #t2 = time.time()
    #print (t2-t1)*100000
    eig = lg.eigvals(L)
    #t3 = time.time()
    #print (t3-t2)*100000
    # sort like l1 > l2 > l3
    eig = np.sort(eig)
    eig = eig[::-1]
    #t4 = time.time()
    #print (t4-t3)*100000
    # Is it a vortex?
    # Not to begin with, check l2 (turning point)
    return eig[1]
#Example:
# jacc = np.array([[1,2,3],[4,5,6],[7,8,9]])
# a, b = l2(jacc)
# print a, b

#a = l2(np.array([[  2.33069279e-08 , 1.15848128e-10 , -5.53924094e-11],
 #[  1.18193799e-10 ,  2.33149917e-08 , -5.54082857e-11],
 #[ -6.56496404e-11 , -5.75887231e-11  ,-4.66219199e-08]]))
    
#jac = np.array([[1,2,3],[2,3,4],[5,4,3]])

#print l2(jac)

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:48:36 2018

@author: Sasha
"""

import numdifftools as nd
import numpy as np


from math import *
#This is creating Tiago's interval, from 0 to 2pi. 
#The last term in N: the number of terms in the interval.
interval = np.linspace(0,2*pi,100)
print interval

#Unnecessary check whether the interval works
#u = interval[99] - 2*pi

#Define the Numpy Sine function.
def fun(x):
    return np.sin(x)
    
#Use actual Jacobian stuff: jac is for default Order 1,
#and jac2 is for an order 50. You can change this order yourself.
jac = nd.Jacobian(fun)(interval)
order2 = 50
jac2 = nd.Jacobian(fun, order=order2)(interval)
grad = nd.Gradient(fun)(interval)

#Check whether the Jacobian is equal to gradient at a point:
check1 = jac[2,3]-grad[2,3]
if check1 == 0.:
    print "Jacobian equals gradient, ok"

#IMPORTANT BIT: Check the error between orders of
#numerical differentiation
error = jac[3,3] - jac2[3,3]
print "The error between Order 1 and Order ", order2, " Jacobians is: ", error






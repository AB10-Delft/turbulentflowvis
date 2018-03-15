#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:12:08 2018

@author: TimBurgers
"""



for i in range(192):
    for j in range(192):
        for k in range(192):
            J_a = J[i][j][k] 
            Q = (J_a[1][1]*J_a[2][2] - J[1][2]*J[2][1]) +(J_a[1][1]*J_a[3][3] - J[1][3]*J[3][1]) + (J_a[2][2]*J_a[3][3] - J[2][3]*J[3][2])
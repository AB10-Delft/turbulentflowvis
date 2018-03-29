import matplotlib as mplt
import numpy as np
from numpy import linalg as lg

def l2(jac):
    jacT = jac.transpose()
    #S and Omega, the main parameters of the method
    S = (jac + jacT) / 2
    O = (jac - jacT) / 2
    #Intermediate step, S^2 + O^2: ELEMENT-WISE!
    L = np.multiply(S,S) + np.multiply(O,O)
    #print L
    eig, eigv = lg.eig(L)
    # sort like l1 > l2 > l3
    eig = np.sort(eig)
    eig = eig[::-1]
    #print eig
    # Is it a vortex?
    # Not to begin with, check l2 (turning point)
    vortex = False
    if eig[1] < 0:
        vortex = True
    #print vortex

    return vortex, eig[1]

#Example:
# jacc = np.array([[1,2,3],[4,5,6],[7,8,9]])
# a, b = l2(jacc)
# print a, b

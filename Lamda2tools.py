import numpy as np
from numpy import linalg as lg

def l2(jac):
    jacT = jac.transpose()
    #S and Omega, the main parameters of the method
    S = (jacT + jac) / 2.
    O = (jacT - jac) / 2.
    #Intermediate step, S^2 + O^2
    L = np.matmul(S,S) + np.matmul(O,O)
    eig, eigv = lg.eig(L)
    # sort like l1 > l2 > l3
    eig = np.sort(eig)
    eig = eig[::-1]
    # Is it a vortex?
    # Not to begin with, check l2 (turning point)
    return eig[1]

import numpy as np
from numpy import linalg

def computeSandO(J): # J has to be a 3x3 array
    S = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    O = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    for i in range(3):
        for j in range(3):
            S[i][j] = 0.5*(J[j][i]+J[i][j])
            O[i][j] = 0.5*(J[j][i]-J[i][j])

    return S,O

def computeA(S,O):
    return np.dot(S,S)+np.dot(O,O)

def evaluenegative(x): #input x: evalue2, if 1 is output, then second eigenvalue is negative, if 0 it is positive
    if x<0:
        a = 1
    else:
        a = 0
    return a

def sortedeigenvalues(M): #insert a 'matrix' like a array as [[a,b,c],[d,e,f],[g,h,i]], so the rows of the matrix as seperate lists
    evalues,y = linalg.eig(M)
    evalues = np.sort(evalues)
    return evalues[1]

def lambda2method(J):
    S,O = computeSandO(J)
    A = computeA(S,O)
    evalues = sortedeigenvalues(A)
    x = evaluenegative(evalues)
    return x
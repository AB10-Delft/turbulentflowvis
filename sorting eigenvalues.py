import numpy as np
from numpy import linalg as LA

#insert a matrix at 'HERE' as [[a,b,c],[d,e,f],[g,h,i]], so the rows of the matrix as seperate lists

evalues,y = LA.eig(np.array('HERE'))
evalues = np.sort(evalues)

print evalues

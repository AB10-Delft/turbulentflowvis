# make sure you've imported all the functions
from alldefs import *
import numpy as np
import time
start_time = time.time()

for i in range(0,1000000):
    J = [[1,2,3,],[i,2,4],[2,2,3]]
    x = lambda2method(J)
print x
print("--- %s seconds ---" % (time.time() - start_time))

import numpy as np

A = np.zeros((3,3,3))

r = range(0,3)

i = 0
j = 0
k = 0
val = 1

running = True

while running:
    A[i,j,k] = val
    val = val+1
    k = k+1
    if k == 3:
        k = 0
        j = j+1
    if j == 3:
        j = 0
        i = i+1
    if i == 3:
        running = False


print "whole array: "
print A
print
print "i gives the plane: "
print "A[0] = "
print A[0]
print
print "j gives the row in the plane: "
print "A[0,0] = "
print A[0,0]
print
print "k gives the column in the row in the plane: "
print "A[0,0,1] = ", A[0,0,1]
        


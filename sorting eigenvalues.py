def sortedeigenvalues(M): #insert a 'matrix' like a array as [[a,b,c],[d,e,f],[g,h,i]], so the rows of the matrix as seperate lists
    evalues,y = linalg.eig(np.array([[1,-1],[1,-1]]))
    evalues = np.sort(evalues)
    return evalues
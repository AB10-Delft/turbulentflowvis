def computeSandO(J): # J has to be a 3x3 array
    S = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    O = np.array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    for i in range(3):
        for j in range(3):
            S[i][j] = 0.5*(J[j][i]+J[i][j])
            O[i][j] = 0.5*(J[j][i]-J[i][j])

    return S,O
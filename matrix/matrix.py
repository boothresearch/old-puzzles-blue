import numpy as np
class Matrix(object):

    def __init__(self, matrix_string):
        M = matrix_string.split("\n")
        rsize = len(M)
        csize = len(M[0].split(" "))       
        a= np.array([[0 for i in range(csize)]]*rsize )
        self.a = a
        for i in range(rsize):
            ro = M[i].split(" ")
            for j in range(csize):
                a[i][j] = ro[j]

    def row(self, index):      
        t = self.a[index-1,:]
        print(t)

    def column(self, index):
        t = self.a[:,index-1]
        print(t)
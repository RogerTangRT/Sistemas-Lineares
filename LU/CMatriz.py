import numpy as np
import os


class CMatriz():
    # Construtor
    def __init__(self, matrizDescription):
        os.system('cls')
        self.A = np.mat(matrizDescription)
        self.L = np.zeros(self.A.shape[0])
        self.U = np.zeros(self.A.shape[0])
        self.M = np.zeros(self.A.shape[0])

    def mostraMatrixA(self):
        print("Matrix A")
        print(self.A)

    def mostraMatrixL(self):
        print("Matrix L")
        self.calculaMatrixU()
        print(self.L)

    def calculaMatrixU(self):
        for lin in range(1, self.A.shape[0]):
            print(lin)
            print(self.A[lin, 0])
            print(self.A[0, 0])
            x = self.A[lin, 0]/self.A[0, 0]
            self.U[lin, 0] = x

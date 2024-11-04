import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
#Las matrices tienen que tener np.array([[],[]]) esta forma
 
B = np.array([[11, 12, 13],
              [14, 15, 16]])
# orden de una matriz
print(A.shape)
# (2, 3)
# dos filas, tres columnas

# suma y resta
C = A + B
print(C)

#Ponderacion
E = 2*A
print(E)
# [[ 2 4 6]
# [ 8 10 12]]

# transposici ́on
F = A.T
print(F)

#multiplicar matriz
T = F.dot(B)
print(T)
#[[ 67  72  77]
# [ 92  99 106]
# [117 126 135]]
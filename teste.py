import numpy as np
from funcoes import criarMatriz, printMatriz, printVetor

a = criarMatriz(3,2)

a[0][0] = 1
a[0][1] = 2
a[1][0] = 1
a[1][1] = 1
a[2][0] = 1
a[2][1] = -1

u, s, v = np.linalg.svd(a)

print("MATRIZ A")
printMatriz(a)

print("matriz U")
printMatriz(u)

print("\nMATRIZ S")
printVetor(s)

print("Matriz V")
printMatriz(v)
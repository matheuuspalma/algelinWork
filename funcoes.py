#Universidade Federal do Rio de Janeiro
#Escola Politécnica
#Departamento de Engenharia Eletrônica e de Computação
#Algebra Linear II - Prof.: Marcelo Campos
#Grupo 2

def printMatriz(m):

    i = len(m)
    j = len(m[0])

    print()
    for linhas in range (0, i, 1):
        print("")
        for colunas in range(0, j, 1):
            print(" ", m[linhas][colunas], end = "")
    return 0

def setMatriz(matriz):

    print(" Prenchendo a matriz", len(matriz)," X ", len(matriz[0]))
    print("Obs: preencha na ordem das linhas, da esqueda para a direita!")

    for linhas in range(len(matriz)):
        print("")
        for colunas in range(len(matriz[0])):
            matriz[linhas][colunas] = int(input())

    return 0

def transposta(m):

    i = len(m)  #linhas
    j = len(m[0])   #colunas

    transposta = criarMatriz( j, i)
    for linhas in range (0, i, 1):
        for colunas in range(0, j, 1):
            transposta[colunas][linhas] = m[linhas][colunas]

    return transposta

def criarMatriz( linhas, colunas):

    matriz = [0]*linhas

    for i in range (linhas):
        matriz[i] = [0]*colunas
    return matriz

# def decomposicaoPLU(m, l, u, p):

def multiplicacaoMatrizes(a,b):

    resultado = criarMatriz((len(a), len(b[0]))   # A mXn e B nXj   matriz resultado é R mXj
    
    if( len(a[0]) != len(b)):
        return -1
    

    for linhas in range(len(a)):
        soma = 0
        i = 0
        for colunas in range(len(a[0])):
            soma += a[linhas][colunas]*b[colunas][i]
            

    
        resultado = soma



    
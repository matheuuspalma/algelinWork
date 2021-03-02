#Universidade Federal do Rio de Janeiro
#Escola Politécnica
#Departamento de Engenharia Eletrônica e de Computação
#Algebra Linear II - Prof.: Marcelo Campos
#Grupo 2

import copy

def printMatriz(m):

    i = len(m)
    j = len(m[0])

    print()
    for linhas in range (0, i, 1):
        print("")
        for colunas in range(0, j, 1):
            string = str(round(m[linhas][colunas], 2))
            print("| ", string , end = "\t")

    print("")
    return 0

def setMatriz(matriz):        

    fileMatriz = open("dados_02.csv","r")

    content = fileMatriz.readlines()

    value = ""
    for i in range( 1 ,len(matriz)+1,1):
        k = 0
        if(len(matriz[0])== 4):
                while(content[i][k] != ","): #para pular o id
                    k += 1
                k += 1
        for j in range(len(matriz[0])):
            while( content[i][k] != "," and k < len(content[i])):
                value += content[i][k]
                k += 1
            k += 1
            matriz[i - 1][j] = float(value)
            value = ""

    fileMatriz.close()      

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

def decomposicaoPLU(a,p,l,u):  #sistema linar Ax=b || A matriz a será decomposta em PLU

    if( a == "" or l == "" or p == "" or u == ""):
        return -1

    nLinhas = len(a)
    nColunas = len(a[0])

    m = 0   #m = x[1n]/x[2n] preenchimento da matriz lower
    i = 0
    j = 0 

    for i in range(nLinhas):
        u[i] = a[i].copy()
        for j in range(nColunas):
            if( i == j):
                p[i][j] = 1
                l[i][j] = 1

    print("*** Matriz U = A: ***")
    printMatriz(u)

    j = 0
    while (j < nColunas - 1):
        i = j
        pivoteamento(a,p,j)
        while(i < nLinhas - 1):
            m = u[i + 1][j]/u[j][j]
            if ( j <= i):
                l[i + 1][j] = m
                k = j
            while(k < nColunas):   
                u[i + 1][k] = u[i + 1][k] - m*u[j][k]         
                k += 1
            i += 1
        j += 1
    return 0

def pivoteamento(m,p,nColuna):
    linhas = len(m)
    

    i = 0
    while( i < linhas) - 1:
        if(m[i] < m[i + 1]):
            aux = m[i]
            m[i] = m[i + 1]
            m[i + 1] = aux
            aux = p[i]
            p[i] = p[i + 1]
            p[i + 1] = aux
    return 0


def multiplicacaoMatrizes(a,b):

    resultado = criarMatriz(len(a), len(b[0]))   # A mXn e B nXj   matriz resultado é R mXj
    
    if(len(a) != len(b[0]) ):
        return -1
    
    linhas = 0
    i = -1
    while(linhas < len(a)):
        soma = 0
        i += 1
        for colunas in range(len(a[0])):
            soma += a[linhas][colunas]*b[colunas][i]
        resultado[linhas][i] = soma
        
        if(i == (len(resultado[0]) - 1)):
            i = -1
            linhas += 1

    return resultado    

    




    
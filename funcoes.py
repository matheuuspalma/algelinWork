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

def setVetor(nameFile):
    
    m = criarMatriz(15,5)
    v = [0]*15

    setMatriz(m, nameFile)

    for i in range(15):
        v[i] = m[i][4]
    

    return v

def setMatriz(matriz, nameFile):        

    fileMatriz = open(nameFile + ".csv","r")

    content = fileMatriz.readlines()

    value = ""
    for i in range( 1 ,len(matriz)+1,1):
        k = 0
        if(len(matriz[0])== 3):
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
                u[i + 1][k] = u[i + 1][k] - (m*u[j][k])         
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


def backSubstitutionLower(a, b): # sistema linar Ax=B

    x = [0]*len(b)

    x[0] = b[0]/a[0][0]
    x[1] = (b[1] - a[1][0]*x[0])/a[1][1]
    x[2] = (b[2] - a[2][0]*x[0] - a[2][1]*x[1])/a[2][2]

    if(len(b) == 4):
        x[3] = (b[3] - a[3][0]*x[0] - a[3][1]*x[1] - a[3][2]*x[2])/a[3][3]
       
    return x

def backSubstitutionUpper(a, b): # sistema linar Ax=B

    x = [0]*len(b)

    if(len(b) == 4):
        x[3] = (b[3])/a[3][3]
        x[2] = (b[2] - a[2][3]*x[3])/a[2][2]
        x[1] = (b[1] - a[1][3]*x[3] - a[1][2]*x[2])/a[1][1]
        x[0] = (b[0] - a[0][3]*x[3] - a[0][2]*x[2] - a[0][1]*x[1])/a[0][0]
    else:
        x[2] = (b[2])/a[2][2]
        x[1] = (b[1] - a[1][2]*x[2])/a[1][1]
        x[0] = (b[0] - a[0][2]*x[2] - a[0][1]*x[1])/a[0][0]

    return x

def multiplicacaoMV(m,v):

    linhas = len(m)
    colunas = len(m[0])

    resultado =[0]*linhas

    if( colunas != len(v)):
        return -1

    for i in range(linhas):
        soma = 0
        for j in range(colunas):
            soma += m[i][j]*v[j]

        resultado[i] = soma

    return resultado

def printVetor(v):

    for i in range(len(v)):
        string = str(round(v[i], 4))
        print(string, end  = "\t")

    print("\n")
    return 0
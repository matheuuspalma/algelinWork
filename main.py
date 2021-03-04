#Universidade Federal do Rio de Janeiro
#Escola Politécnica
#Departamento de Engenharia Eletrônica e de Computação
#Algebra Linear II - Prof.: Marcelo Campos
#Grupo 2

from funcoes import criarMatriz, printMatriz, transposta, setMatriz, multiplicacaoMatrizes, decomposicaoPLU, backSubstitutionLower, setVetor, multiplicacaoMV, backSubstitutionUpper, printVetor

def main():

    print(" *******************  ALGEBRA LINEAR II *********************")
    print("\nEntre com as dimensões da matriz A: ")

    j = int(input("N colunas: ")) # tem que ser 3 ou 4

    m1 = criarMatriz(15, j)
    m2 = criarMatriz(15, j)
    m3 = criarMatriz(15, j)

    setMatriz(m1,"01")
    setMatriz(m2,"02")
    setMatriz(m3,"03")

    t1 = transposta(m1)
    t2 = transposta(m2)
    t3 = transposta(m3)

    aproximacao1 = multiplicacaoMatrizes(t1, m1)
    aproximacao2 = multiplicacaoMatrizes(t2, m2)
    aproximacao3 = multiplicacaoMatrizes(t3, m3)

    #******************** setosa **************************
    u1 = criarMatriz(len(aproximacao1), len(aproximacao1[0]))
    l1 = criarMatriz(len(aproximacao1), len(aproximacao1[0]))
    p1 = criarMatriz(len(aproximacao1), len(aproximacao1[0]))
    v1 = setVetor("01") #petal width
    b1 = multiplicacaoMV(t1,v1) #Ax = *b* MULTIPLICAÇÃO DA TRASVERSA COM A COLUNA ALTA E MAGRA PETAL WIDTH

    decomposicaoPLU(aproximacao1, p1, l1, u1)

    y1 = backSubstitutionLower(l1,b1)
    
    result1 = backSubstitutionUpper(u1,y1)
    
    print(" RESULTADO SETOSA :")
    printVetor(result1)

    
    #********************** versicolor ********************
    u2 = criarMatriz(len(aproximacao2), len(aproximacao2[0]))
    l2 = criarMatriz(len(aproximacao2), len(aproximacao2[0]))
    p2 = criarMatriz(len(aproximacao2), len(aproximacao2[0]))
    v2 = setVetor("02") #petal width
    b2 = multiplicacaoMV(t2,v2) #Ax = *b* MULTIPLICAÇÃO DA TRASVERSA COM A COLUNA ALTA E MAGRA PETAL WIDTH

    decomposicaoPLU(aproximacao2, p2, l2, u2)

    y2 = backSubstitutionLower(l2,b2)

    result2 = backSubstitutionUpper(u2,y2)
    
    print(" RESULTADO VERSICOLOR :")
    printVetor(result2)

    
    #********************** virginica ********************

    u3 = criarMatriz(len(aproximacao3), len(aproximacao3[0]))
    l3 = criarMatriz(len(aproximacao3), len(aproximacao3[0]))
    p3 = criarMatriz(len(aproximacao3), len(aproximacao3[0]))
    v3 = setVetor("03") #petal width
    b3 = multiplicacaoMV(t3,v3) #Ax = *b* MULTIPLICAÇÃO DA TRASVERSA COM A COLUNA ALTA E MAGRA PETAL WIDTH

    decomposicaoPLU(aproximacao3, p3, l3, u3)

    y3 = backSubstitutionLower(l3,b3)

    result3 = backSubstitutionUpper(u3,y3)
    
    print(" RESULTADO VIRGINICA :")
    printVetor(result3)

    printMatriz(aproximacao1)
    return 0


main()

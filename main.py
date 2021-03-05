#Universidade Federal do Rio de Janeiro
#Escola Politécnica
#Departamento de Engenharia Eletrônica e de Computação
#Algebra Linear II - Prof.: Marcelo Campos
#Grupo 2

from funcoes import criarMatriz, printMatriz, transposta, setMatriz, multiplicacaoMatrizes, decomposicaoPLU, backSubstitutionLower, setVetor, multiplicacaoMV, backSubstitutionUpper, printVetor
import numpy as np

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
    

    print("**************************************")
    print(" RESULTADO SETOSA :")

    print("\nMATRIZ A: ")
    printMatriz(aproximacao1)

    print("\nMATRIZ P :")
    printMatriz(p1)

    print("\nMATRIZ L : ")
    printMatriz(l1)

    print("\nMATRIZ U:")
    printMatriz(u1)

    print("\nCoeficientes: ")
    printVetor(result1)
    print("\n\nDECOMPOSIÇÂO ESPECTRAL: \n\n")

    uh1, s1, vh1 = np.linalg.svd(aproximacao1)

    print("\nMATRIZ U:")
    printMatriz(uh1)
    print("\nMATRIZ S:")
    printVetor(s1)
    print("\nMATRIZ V:")
    printMatriz(vh1)
    
    
    print("\n**************************************")

    #********************** versicolor ********************
    u2 = criarMatriz(len(aproximacao2), len(aproximacao2[0]))
    l2 = criarMatriz(len(aproximacao2), len(aproximacao2[0]))
    p2 = criarMatriz(len(aproximacao2), len(aproximacao2[0]))
    v2 = setVetor("02") #petal width
    b2 = multiplicacaoMV(t2,v2) #Ax = *b* MULTIPLICAÇÃO DA TRASVERSA COM A COLUNA ALTA E MAGRA PETAL WIDTH

    decomposicaoPLU(aproximacao2, p2, l2, u2)

    y2 = backSubstitutionLower(l2,b2)

    result2 = backSubstitutionUpper(u2,y2)
    
    print("**************************************")
    print(" RESULTADO VERSICOLOR :\n")

    print("MATRIZ A: ")
    printMatriz(aproximacao2)

    print("\n MATRIZ P :")
    printMatriz(p2)

    print("\nMATRIZ L : ")
    printMatriz(l2)

    print("\nMATRIZ U:")
    printMatriz(u2)

    print("\nCoeficientes: ")
    printVetor(result2)

    print("\n\nDECOMPOSIÇÂO ESPECTRAL: \n\n")

    uh2, s2, vh2 = np.linalg.svd(aproximacao2)

    print("\nMATRIZ U:")
    printMatriz(uh2)
    print("\nMATRIZ S:")
    printVetor(s2)
    print("\nMATRIZ V:")
    printMatriz(vh2)
    
    print("\n**************************************")

    
    #********************** virginica ********************

    u3 = criarMatriz(len(aproximacao3), len(aproximacao3[0]))
    l3 = criarMatriz(len(aproximacao3), len(aproximacao3[0]))
    p3 = criarMatriz(len(aproximacao3), len(aproximacao3[0]))
    v3 = setVetor("03") #petal width
    b3 = multiplicacaoMV(t3,v3) #Ax = *b* MULTIPLICAÇÃO DA TRASVERSA COM A COLUNA ALTA E MAGRA PETAL WIDTH

    decomposicaoPLU(aproximacao3, p3, l3, u3)

    y3 = backSubstitutionLower(l3,b3)

    result3 = backSubstitutionUpper(u3,y3)
    print("\n**************************************")
    print(" RESULTADO VIRGINICA :")

    print("\nMATRIZ A: ")
    printMatriz(aproximacao3)

    print("\nMATRIZ P :")
    printMatriz(p3)

    print("\nMATRIZ L : ")
    printMatriz(l3)

    print("\nMATRIZ U:")
    printMatriz(u3)

    print("\nCoeficientes: ")
    printVetor(result3)

    print("\n\nDECOMPOSIÇÂO ESPECTRAL: \n\n")

    uh3, s3, vh3 = np.linalg.svd(aproximacao3)

    print("\nMATRIZ U:")
    printMatriz(uh3)
    print("\nMATRIZ S:")
    printVetor(s3)
    print("\nMATRIZ V:")
    printMatriz(vh3)
    
    return 0


main()

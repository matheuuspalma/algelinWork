#Universidade Federal do Rio de Janeiro
#Escola Politécnica
#Departamento de Engenharia Eletrônica e de Computação
#Algebra Linear II - Prof.: Marcelo Campos
#Grupo 2

from funcoes import criarMatriz, printMatriz, transposta, setMatriz

def main():

    print(" *******************  ALGEBRA LINEAR II *********************")
    print("\nEntre com as dimensões da matriz A: ")

    i = int(input("N linhas: "))
    j = int(input("N colunas: "))

    m = criarMatriz(i, j)

    setMatriz(m)

    printMatriz(m)

    t = transposta(m)

    printMatriz(t)

    return 0

main()

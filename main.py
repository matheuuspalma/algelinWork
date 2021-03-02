#Universidade Federal do Rio de Janeiro
#Escola Politécnica
#Departamento de Engenharia Eletrônica e de Computação
#Algebra Linear II - Prof.: Marcelo Campos
#Grupo 2

from funcoes import criarMatriz, printMatriz, transposta, setMatriz, multiplicacaoMatrizes, decomposicaoPLU

def main():

    print(" *******************  ALGEBRA LINEAR II *********************")
    print("\nEntre com as dimensões da matriz A: ")

    i = int(input("N linhas: "))
    j = int(input("N colunas: "))

    m = criarMatriz(i, j)

    setMatriz(m)

    t = transposta(m)

    resultado = multiplicacaoMatrizes(t, m)

    u = criarMatriz(len(resultado), len(resultado[0]))
    l = criarMatriz(len(resultado), len(resultado[0]))
    p = criarMatriz(len(resultado), len(resultado[0]))

    decomposicaoPLU(resultado, p, l, u)
    print("\n*** Matriz resultado: ***")
    printMatriz(resultado)
    print("\n*** Matriz P: ***")
    printMatriz(p)
    print("\n*** Matriz L: ***")
    printMatriz(l)
    print("\n *** Matriz U: ***")
    printMatriz(u)
    return 0

main()

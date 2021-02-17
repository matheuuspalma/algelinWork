/*Universidade Federal do Rio de Janeiro
  Escola Politécnica
  Algebra Linear
*/

#include <main.h>
#include <stdio.h>

char fatoracao(long int m, int a, int b){ // m seria a matriz, b e c suas dimensões

    long int l[100][100]; //matriz lower (triangular inferior)
    long int u[100][100]; //matriz upper (triangular superior)
    long double aux;
    int i,j;


    if( m == NULL || a == NULL || b == NULL){
        exit("Argumento Inválido. Entre com uma matriz e suas dimensões!");
    }

    for( j = 0; j < b; j++){  //preenchendo a primeira linha da matriz U, que é igual a primeira linha da matriz m
        u[0][j] = m[0][j];
    }

    for(i = 0; i < a - 1;  i++){

        aux = m[i+1][j]/m[i][j];
        
        for(j = 0; j < b; j++){     //linha 2 = l2 - aux*l1  

            if( i == j){
                l[i][j] = 1;
            }else if( j > i){
                l[i][j] = 0;
            }else{      
                l[i][j] = aux;
            }

            u[i + 1][j] = m[i+1][j] - aux(m[i][j]);

        }
    }

    return 0;
}
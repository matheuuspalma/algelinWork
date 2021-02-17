/*Universidade Federal do Rio de Janeiro
  Escola Politécnica
  Algebra Linear
*/

#include "main.h"
#include <stdio.h>


int main(){

    int l,c,i,j;
    long int m[100][100];

    printf(" **************  A x = b ************ \n");

    printf(" Entre com as dimensoes da matriz A: \n");
    
    printf(" Numero de linhas : ");
    scanf("%d", &l);
    printf(" Numero de colunas: ");
    scanf("%d", &c);


    printf(" Preencha com os valores da matriz A: \n\n");

    for (i = 0; i < l; i++){
      for(j = 0; j < c; j++){
        
        scanf("%ld", &m[i][j]);

      }
    }  


    printf(" Matriz A %d X %d :", l, c);
    
    for (i = 0; i < l; i++){
      printf("\n");
      for(j = 0; j < c; j++){
        
        printf(" %ld ", m[i][j]);

      }
    }  

    printf("\n");

    //while( aux != "fim"){

    //fatoracao( a, b, c , d);


    return 0;
               
}




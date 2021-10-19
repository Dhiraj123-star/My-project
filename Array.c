//array in C
#include<stdio.h>
int main(){
    int i=0;
    int marks[5]; //declaring of the array
    marks[0]=100;
    marks[1]=90;
    marks[2]=93;
    marks[3]=89;
    marks[4]=76;
    //traversal of the array
    for(i=0;i<5;i++){
        printf("%d\n",marks[i]);
    }//end of the for loop
    printf("Thanks for using C :)");
}
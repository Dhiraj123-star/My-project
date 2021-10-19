#include<stdio.h>
int main(){
    char t[50];
    printf("Enter Your Another String :\n");
    scanf("%[^\n]s",t);  //take input the whitespace also
    printf("your Entered string is :\n%s",t);

}
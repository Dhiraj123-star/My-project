//pointers with the string
#include<stdio.h>
int main(){
    char s[11]="C program";
    char *p=s; //pointer p is pointing to string s
    printf("%s",p); //string is printed if we print p
}
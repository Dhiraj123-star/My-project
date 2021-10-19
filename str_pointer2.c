//pointer to copy the content of a string into another
#include<stdio.h>
int main(){
    char* ptr="Hello C programming";
    printf("String ptr: %s\n",ptr);
    char* ptr1;
    printf("copying the content of ptr into ptr1 :\n");
    ptr1=ptr;
    printf("String ptr1: %s\n",ptr1);
}
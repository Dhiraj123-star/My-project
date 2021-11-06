#include<stdio.h>

union abc{
    int a ;
    char c;
};

int main(int argc, char const *argv[])
{
    union abc *ptr ; //pointer variable declaration

    union abc var;

    var.a=100;

    var.c = 'E';

    ptr= &var;

    printf("The value of a is: %d",ptr->a);

    printf("\nThe value of c is: %c",ptr->c);
    
    return 0;
}

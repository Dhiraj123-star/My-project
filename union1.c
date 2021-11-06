#include<stdio.h>

//union example

union unionEx{

    int a;
    char b;
    double d;
}var; 

int main(int argc, char const *argv[])

{
    var.a = 100;
    var.b = 'D';
    var.d=12.455;

    printf("a is %d",var.a);

    printf("\n b is %c",var.b);

    printf("\nThe size of the union is: %d",sizeof(union unionEx));


    
    return 0;
}

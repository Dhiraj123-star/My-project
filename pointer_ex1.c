//pointer example in C
#include <stdio.h>
int main(int argc, char const *argv[])
{
    //pointer declaration

    int* p ; //here p is pointer of int type
    int a ;
    a=10 ; //assign value 10 to a
    p=&a ; //assign address of a to the p
     printf("The value of a is: %d\n",a);
     printf("The address of a is :%d\n",&a);
     printf("The address in pointer p is: %d\n",p);
     printf("the value in the pointer p is: %d\n",*p);
     printf("Thanks for using C programming Language :)");
    return 0;
}

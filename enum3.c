//enum with bitwise operator
#include<stdio.h>

enum design{
    bold =1,
    italics=4,
    underline=2
};
int main(int argc, char const *argv[])
{
    int design= underline|italics; // (|) bitwise or operator

    printf("The value is %d\n", design);

    printf("Thanks for using C programming language :)");
    return 0;
}

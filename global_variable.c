#include<stdio.h>

//global variable declaration

int a=10; 

void displayme(); //function definition

int main(int argc, char const *argv[])
{
    a++; //increment by 1

    displayme(); //calling the function

    return 0;
}
void displayme()
{

    a++; ///increment by 1

    printf("The value of a is: %d",a);
}

#include<stdio.h>
#include<string.h>

int main(int argc, char const *argv[])
{

    char name[30]; //array of string

    printf("Enter your name: ");

    gets(name);

    printf("Name: ");

    puts(name);
    
    return 0;
}

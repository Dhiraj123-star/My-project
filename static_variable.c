#include<stdio.h>

void display(); //function declaration

int main(int argc, char const *argv[])
{
    
    //calling the function
display();
display();

    return 0;
}
void display(){ //function definition
    static int i=10;
    
    i+=10; //increment by 10

    printf("The value of i is: %d\n",i);
}

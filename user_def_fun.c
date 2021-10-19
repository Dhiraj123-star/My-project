//user defined function
#include<stdio.h>
int sumnum(int,int); //function declaration
int main(int argc, char const *argv[])
{
    int a,b , r;
    
    printf("Enter Your first number:");
    scanf("%d",&a);
    printf("Enter your Second number: ");
    scanf("%d",&b);
    r=  sumnum(a,b);
    printf("The sum is :%d\n",r);

    printf("Thanks for using C programmig language :)");

    return 0;
}
//function definitation
int sumnum(int n1,int n2){
    int sum1=n1+n2;
    return sum1;
}

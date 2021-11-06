#include<stdio.h>

int reverseNum(int num){
    int rev=0;
    while(num>0){

        int mynum= num%10;
        rev=rev*10+mynum;
        num=num/10;
    }
    return rev;

}
int main(int argc, char const *argv[])
{
    int number;

    printf("Enter your Number: ");

    scanf("%d",&number);

//calling the function

int result = reverseNum(number);

printf("The reversed number is: %d",result);
    

    return 0;
}

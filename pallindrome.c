#include<stdio.h>

int main(int argc, char const *argv[])
{
    int n,r, sum=0, temp;

    printf("Enter your number: ");
    scanf("%d",&n);

    temp=n;

    while(n>0){

        r= n%10;
        sum=(sum*10)+r;
        n=n/10;
    }

    if(temp==sum){
        printf("Pallindrome number");
    }
    else{
        printf("Not pallindrome number");
    }
    
    return 0;
}

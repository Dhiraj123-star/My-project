//recursion in c
#include<stdio.h>
int sum(int n);

int main(int argc, char const *argv[]){

int num,result;

printf("Enter your number :");

scanf("%d",&num);

result=sum(num);
printf("the result is: %d",result);

    return 0;
}

int sum(int  n){
    if(n!=0){
        return n + sum(n-1);

    }else{
        return n;
    }
}
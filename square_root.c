//find the square root of an inputted number
#include<stdio.h>

#include<math.h>

int main(int argc, char const *argv[])
{
    int mynum;
    
    printf("Enter your number:\n");
    scanf("%d",&mynum);

    float root=sqrt(mynum);

    printf("The square root is: %f",root);

    return 0;
}

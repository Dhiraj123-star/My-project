//another example of pointer in c
#include<stdio.h>
int main(int argc, char const *argv[])
{
    //pointer example
    int *p1; //pointer variable
    int d=10;

    printf("The address of the d is: %p\n",&d);
    printf("The value of the d is :%d\n",d);//10

    p1=&d;

    printf("The address of d in pointer is:%p\n",p1);
    printf("The value of d in pointer is: %d\n",*p1);//10
   
   d=12; //reassign the value of d

   printf("The address of d in pointer is:%p\n",p1);
   printf("The value of d in pointer is: %d\n",*p1);//12
  
  *p1 =31; //change the value of pointer 
  printf("The address of the d is: %p\n",&d);
  printf("The value of the d is :%d\n",d);//31

    return 0;
}

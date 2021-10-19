//structure example in c
#include<stdio.h>

struct  mydata
{
    int rank;
    
} ;
int main(int argc, char const *argv[])
{
     struct mydata obj1;

     obj1.rank=1;
     
     printf("the rank is: %d", obj1.rank);





    return 0;
}

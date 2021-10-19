#include<stdio.h>

//union and struct size example


union employee
{
    float salary; //size is 4
    int studint;  //size is 4
}emp;  //st is union type variable

struct  student1
{
    float  marks; // size is 4
    int st_id;  //size is 4

}st1;

int main(int argc, char const *argv[])
{
    //the size of the union

    printf("the size of the union type is: %d\n",sizeof(emp)); //returns 4 

    printf("the size of the struct type is: %d",sizeof(st1)); // returns  8

    return 0;
}




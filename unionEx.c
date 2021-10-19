#include<stdio.h>

//union example

union employee{
    int empid;
    int empage;

}emp;

int main(int argc, char const *argv[])
{ 
    //setting the id of employee
    emp.empid=101;
    //emp.empage=23;
    

    printf("The id of the employee is: %d\n",emp.empid);
    //printf("The age of the employee is: %d",emp.empage);


    return 0;
}

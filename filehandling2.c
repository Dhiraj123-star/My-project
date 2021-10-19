//reading from the file
#include<stdio.h>
#include<stdlib.h>
int main(){
    int id;
    char name[30];
    float salary;

    FILE *fptr;
    fptr=fopen("myfile.txt","r");
    fscanf(fptr,"%d",&id);
    printf("The id is: %d\n",id);
    fscanf(fptr,"%s",&name);
    printf("the name is: %s\n",name);
    fscanf(fptr,"%f",&salary);
    printf("the salary is: %f\n",salary);
    fclose(fptr);
    printf("Thanks for using c programming langauge :)");
    
    return 0;


}
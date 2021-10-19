//creating and writing into the file
#include<stdio.h>
#include<stdlib.h>
int main(){
    int id;
    char name[30];
    float salary;

    FILE *fptr;
    fptr=fopen("myfile.txt","w");
    printf("Enter Your id: ");
    scanf("%d",&id);
    fprintf(fptr,"%d\n",id);
    printf("Enter Your name: ");
    scanf("%s",&name);
    fprintf(fptr,"%s\n",name);
    printf("Enter your salary: ");
    scanf("%f",&salary);
    fprintf(fptr,"%f\n",salary);
    fclose(fptr);
    return 0;

}
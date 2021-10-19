//writing into the binary file
//file handling in binary 
#include<stdio.h>
#include<stdlib.h>
struct threeNum
{
   int n1, n2, n3;
};

int main()
{
   int n;
   struct threeNum num,num1;
   FILE *fptr;

   if ((fptr = fopen("myfile.bin","wb")) == NULL){
       printf("Error! opening file");

       // Program exits if the file pointer returns NULL.
       exit(1);
   }

   for(n = 1; n < 5; ++n)
   {  
       //first instance value
      num.n1 = n;
      num.n2 = 5*n;
      num.n3 = 5*n + 1;
      //second instance value 
      num1.n1=n*10;
      num1.n2=n*20;
      num1.n3=n*30;
      fwrite(&num, sizeof(struct threeNum), 1, fptr); 
      fwrite(&num1,sizeof(struct threeNum ),1,fptr);
   }
   fclose(fptr); 
   return 0;
}

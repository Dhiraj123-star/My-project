//reading  from the file
#include<stdio.h>
#include<stdlib.h>
struct threeNum
{
   int n1, n2, n3;
};

int main()
{
   int n;
   struct threeNum num ,num1;
   FILE *fptr;

   if ((fptr = fopen("myfile.bin","rb")) == NULL){
       printf("Error! opening file");

       // Program exits if the file pointer returns NULL.
       exit(1);
   }

   for(n = 1; n < 5; ++n)
   {
      fread(&num, sizeof(struct threeNum), 1, fptr); 
      fread(&num1, sizeof(struct threeNum), 1, fptr); 
      
      printf("\nn1: %d\tn2: %d\tn3: %d", num.n1, num.n2, num.n3);
      
      printf("\nn1: %d\tn2: %d\tn3: %d", num1.n1, num1.n2, num1.n3);
      printf("\n");
   }
   fclose(fptr); 
   printf("Thanks for using C programming Language :)");
  
   return 0;
}
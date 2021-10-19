//program for sorting of array
#include<stdio.h>
int main(){
    int i,j,temp;
    int a[10]={10,6,4,7,2,1,3,9,5,8}; //array of the ten elements
    for(i=0;i<10;i++){ //outer loop
        for(j=0;j<10;j++){ //inner loop
            if(a[j]>a[i])
            { 
                //swaping  of elements
                
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    printf("printing the sorted element list: \n");
    for(i=0;i<10;i++){
        printf("%d\n",a[i]);
    }
}
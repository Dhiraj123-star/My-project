//program for finding largest and second largest element from the array
#include<stdio.h>
int main(){
    int arr[50],i,n,largest,sec_largest;
    printf("Enter your size of Array:");
    scanf("%d",&n);
    printf("Enter your elements: ");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]); //taking input from the user
    }
    largest=arr[0]; //store first element of the array in largest variable

    sec_largest=arr[1]; //store second element of the array in sec_largest variable
    for(i=0;i<n;i++){  //loop start from  3rd element of the array 
        if(arr[i]>largest){
            sec_largest=largest;
            largest=arr[i];

        }
        else if(arr[i]>sec_largest && arr[i]!=largest){
            sec_largest=arr[i];
        }
    }
    printf("largest=%d,second largest=%d",largest,sec_largest);
}
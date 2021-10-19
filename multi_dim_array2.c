//multi_dimensional array with input values

#include<stdio.h>

int main(int argc, char const *argv[])
{
    int mymulti[2][3][2];

    printf("Enter your 12 elements\n");

    for(int i=0;i<2;i++){
        for(int j=0;j<3;j++){
            for(int k=0;k<2;k++){
                scanf("%d",&mymulti[i][j][k]);
            }
        }
    }


    printf("Displaying the Array data \n");

for(int i=0;i<2;i++){
        for(int j=0;j<3;j++){
            for(int k=0;k<2;k++){
                printf("mymulti[%d][%d][%d]=%d\n",i,j,k,mymulti[i][j][k]);
            }
            
        }
        
    }
    

    return 0;
}

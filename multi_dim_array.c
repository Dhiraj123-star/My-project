//multi-dimensional Array 
#include<stdio.h>

int main(int argc, char const *argv[])
{
    
int mymulti_dim[2][3]={{12,34,22},{45,56,100}};

for(int i=0;i<2;i++){
    for(int j=0;j<3;j++){
        printf("%d\n",mymulti_dim[i][j]);
    }
    printf("\n");
}



    return 0;
}

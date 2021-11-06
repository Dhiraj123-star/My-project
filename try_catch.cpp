#include<iostream>
using namespace std;

float divison(int x , int y){

    if (y==0){
    throw "Attempted to divide by zero";
    }
    return(x/y);
}

int main(int argc, char const *argv[])
{
    int i=24;
    int j=1;

    float k=0;

    try{
        k=divison(i,j);

    }
    catch(const char *e){
        cerr<<e<<endl;
    }

    cout<<"The result is: "<<k<<endl;
    
    
    return 0;
}

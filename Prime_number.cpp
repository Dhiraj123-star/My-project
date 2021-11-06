//prime number in c++
#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n,i,m=0,flag=0;

    cout<<"Enter your number:  "<<endl;
    cin>>n;

    m=n/2;
    for(i=2;i<=m;i++){

        if(n%i==0){
            cout<<"Number is not prime"<<endl;
            flag=1;
            break;
        }
    }

    if(flag==0){
        cout<<"Number is prime"<<endl;
    }
    

    return 0;
}

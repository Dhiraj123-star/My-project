//reverse number using C++

#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n,reverse =0, rem;

    cout<<"Enter your number: "<<endl;
    cin>>n;

    while(n!=0){

        rem=n%10;
        reverse= reverse*10+rem;
        n=n/10;
    }

    cout<<"Reversed number is: "<<reverse<<endl;
    
    return 0;
}

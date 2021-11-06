#include<iostream>

using namespace std;

int ReverseNum(int num){
    int rev=0;

    while(num>0){

        int mynum= num%10;

        rev=rev*10+mynum;

        num=num/10;
    }
    return rev;
}
int main(int argc, char const *argv[])
{
    int number;

    cout<<"Enter Your number: "<<endl;
    cin>>number;

    //calling the function

    cout<<"The Reversed Number is: "<<ReverseNum(number)<<endl;
    

    return 0;
}

#include<iostream>
#include<deque>
using namespace std;

int main(int argc, char const *argv[])
{
    deque<int> first = {10,30,40};

    //size() function

    cout<<"The size of the deque is: "<<first.size()<<endl;

    if(first.empty()){
        cout<<"Deque is empty"<<endl;
    }
    else{
        cout<<"Deque is not empty"<<endl;
    }

    //another example

    deque<string> deque1 ;

    if(deque1.empty())
    cout<<"deque is empty"<<endl;
    else
    cout<<"deque is not empty"<<endl;
    
    return 0;
}

#include<iostream>
#include<stack>
using namespace std;

void newstack(stack <string> ss){
    stack<string> sg = ss;

    while(!sg.empty()){
        cout<<"\t"<<sg.top();
        sg.pop();

    }
    cout<<endl;
}
int main(int argc, char const *argv[])
{
    stack<string> mystack;

    //adding elements 

    mystack.push("Dhiraj");
    mystack.push("Rohit");
    mystack.push("Yasweer");

    mystack.push("Sachin");

    mystack.push("Ashish");
    mystack.push("Akash");

    cout<<"The stack is: "<<endl;

    newstack(mystack);

    cout<<"The size of the stack is: "<<mystack.size()<<endl;
    cout<<"The top element of the stack is: "<<mystack.top()<<endl;
    cout<<"The pop element of the stack is: ";
    mystack.pop();


    newstack(mystack);


    return 0;
}


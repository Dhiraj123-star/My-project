//stack function in c++
#include<iostream>
#include<stack>
using namespace std;
void newStack(stack<int> ss){
    stack<int> sg=ss;
    while(!sg.empty()){
        cout<<"\t"<<sg.top();
        sg.pop();
    }
    cout<<"\n";
}
int main(int argc, char const *argv[])
{
    stack<int> newst;
    newst.push(100);
    newst.push(200);
    newst.push(300);
    newst.push(400);
    cout<<"The stack newst is: "<<endl;
    newStack(newst);
    cout<<"\n newst size(): "<<newst.size();
    cout<<"\n newst top(): "<<newst.top();
    cout<<"\n newst pop()";
    newst.pop();
    newStack(newst);


    return 0;
}


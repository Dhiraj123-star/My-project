#include<iostream>
#include<queue>

using namespace std;

int main(int argc, char const *argv[])
{
    
    priority_queue<int> p; //variable declaration

    //adding element into the queue

    p.push(100);
    p.push(2);
    p.push(90);
    p.push(8);

    cout<<"The total no. of elements in the queue is: "<<p.size()<<endl;

    while (!p.empty()){
        cout<<p.top()<<endl;
        p.pop();
    }

    
    return 0;
}

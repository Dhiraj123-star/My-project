#include<iostream>
#include<deque>

using namespace std;

int main(int argc, char const *argv[])
{
    deque <int> mydequeue ={12,34,44,55};

    deque <int>::iterator itr = mydequeue.begin() ;
    
    mydequeue.push_back(100); //push_back function

    mydequeue.push_front(10); //push_front function

    mydequeue.insert(itr,2); //insert function

    mydequeue.pop_back(); //removes the last element

    mydequeue.pop_front(); //removes the first element 

    for(itr= mydequeue.begin(); itr!=mydequeue.end();++itr){

        cout<<*itr<<endl;
    }
    
    return 0;
}

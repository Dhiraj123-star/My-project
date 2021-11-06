#include<iostream>
#include<deque>

using namespace std;

int main(int argc, char const *argv[])
{
    deque<string> mydeque = {"Java","C++","Python"};

    deque<string> ::iterator itr;

    //emplace () method

    mydeque.emplace(mydeque.begin(),"Ruby" ); //it adds Ruby at the first position

    //clear method

    mydeque.clear(); //it clears all the elements from the deque

    for(itr=mydeque.begin(); itr!=mydeque.end();++itr){

        cout<<(*itr)<<endl;
    }
    
    
    return 0;
}

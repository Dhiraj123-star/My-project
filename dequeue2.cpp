#include<iostream>
#include<deque>

using namespace std;

int main(int argc, char const *argv[])
{
    deque<string> str = {"C is a programming language"};

    deque<string> str2 = {"JavaScript is famous programming langauge"};

    //swap function

    str.swap(str2);

    deque<string>::iterator itr1 = str.begin();

    deque<string>::iterator itr2 = str2.begin();

    cout<<"After swapping: "<<(*itr1)<<endl;

    cout<<"After swapping: "<<(*itr2)<<endl;


    
    return 0;
}



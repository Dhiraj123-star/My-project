#include<iostream>
#include<deque>

using namespace std;

int main(int argc, char const *argv[])
{
    deque<string> fruits ={"Mango","Papaya","plum","Guava","pineapple"};

    deque<string>::iterator itr;

    cout<<"Contents of the deque is: "<<endl;

    for(itr=fruits.begin(); itr!=fruits.end(); ++itr){
        cout<<(*itr)<<endl;
    }

    //erase function()

    fruits.erase(fruits.begin());

    cout<<endl; //for new line

    cout<<"After erase, the contents of the deque is: "<<endl;

     for(itr=fruits.begin(); itr!=fruits.end(); ++itr){
        cout<<(*itr)<<endl;
    }

    
    return 0;
}

//this is the example of function overriding 
#include<iostream>
using namespace std;
class myclass{
    public:
    void print(){
        cout<<"this is the base class function :)"<<endl;
    }
};

class yourclass:public myclass{
    public:
    void print(){
        cout<<"this is the child class function :)"<<endl;
    }

};
int main()
{
    //creating object
    yourclass obj1;
    obj1.print(); //it will call child class function
    myclass obj2;
    obj2.print(); //it will call parent class function
    return 0;

}
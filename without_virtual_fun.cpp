//without virtual function example
#include<iostream>
using namespace std;
class parent{
    public:
    void showme(){
        cout<<"This is the parent class method :)"<<endl;
    }
};
class child:public parent{
    public:
    void showme(){
        cout<<"this is the child class method :)"<<endl;
    }
};
int main(int argc, char const *argv[])
{
    parent *ptr; //pointer of the base class 
    child ch; //object of the derived class 
    ptr=&ch;
    ptr->showme();//always call parent class method, it can be
    //resolved by using virtual function 
    return 0;
}


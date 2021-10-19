//another example of function overriding
#include<iostream>
using namespace std;
class base{
    public:
    void display(){
        cout<<"This is the base class function"<<endl;

    }
};
class child:public base{
    public:
    void display(){
        cout<<"This is the child class function "<<endl;

    }
};
int main(){
    // access overridden function using pointer
// of Base type that points to an object of Derived class
child c1;
base* ptr= &c1;
ptr->display();  //call the overriden function of the base class
return 0;
}
//virtual function example
#include<iostream>
using namespace std;
class Base{
    public:
    virtual void show()=0; //pure virtual function

};
class Derived_class : public Base{
    public:
    void show(){
        cout<<"This is derived class function"<<endl;

    }
};
int main(int argc, char const *argv[])
{
    //creating object
    Derived_class dr;
    dr.show();
    //another method
    Base *ptr; //creating pointer of base class 
    Derived_class dr1; //creating object of derived class
    ptr=&dr1; //assigning the address of derived_class into 
    //base class
    ptr->show(); //give same output 

    return 0;
}


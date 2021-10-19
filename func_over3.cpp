//invoking overriden function of the base class from derived class
#include <iostream>
using namespace std;
class parent{
    public:
    void print(){
        cout<<"this is the base class method "<<endl;

    }
};
class child:public parent{
    public:
    void print(){
        cout<<"this is the child class method"<<endl;
        //call overriden method
        parent::print();
    }
};
main(){
    //creating object
    child c1;
    c1.print(); //calling child method
    cout<<"Thanks for using C++ programming Language :)"<<endl;
    
}
//more example of function overriding
#include<iostream>
using namespace std;
class c1{
    public:
    void show(){
        cout<<"I'm in the parent class :)"<<endl;

    }
};
class c2:public c1{
    public:
    void show(){
        cout<<"I'm in the child class :)"<<endl;

    }
};
main(){
    //creating objects
    c2 obj1,obj2;
    obj1.show(); //calling child class method
    obj2.c1::show(); //calling parent class method
    cout<<"Thanks for using c++ programming language :)"<<endl;

}

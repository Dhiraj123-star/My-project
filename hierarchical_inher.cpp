//hierarchical inheritance in c++
#include<iostream>
using namespace std;
class science1{
    public:
    void display1(){
        cout<<"This is the science class method"<<endl;

    }
};
class physics:public science1{
    public:
    void display2(){
        cout<<"This is the physics class method"<<endl;
    }
};
class chemistry:public science1{
    public:
    void display3(){
        cout<<"this is chemistry class method "<<endl;
    }
};
int main(int argc, char const *argv[])
{
    
    //creating object of chemistry class
    chemistry ch1;
    ch1.display1(); //calling its own base class method
    ch1.display3(); //calling its own class method

    //creating object of physics classs
    physics p1;
    p1.display1(); //calling its own base class method
    p1.display2(); //calling its own class method

    cout<<"Thanks For using C++ programmig Language :)"<<endl;
    

    return 0;
}


//another example of virtual function
//virtual function allows the base class pointer to access
//the member function of derived class
#include<iostream>
using namespace std;
class myclass{
    public:
    virtual void display(){
        cout<<"This is the base class method "<<endl;
    }
};
class myclass2 :public myclass{
    public:
    void display(){
        cout<<"This is the child class method"<<endl;
    }
};
int main(int argc, char const *argv[])
{

//base class pointer
myclass *mypointer;
myclass2 obj1;
mypointer= &obj1;
mypointer ->display();
    return 0;
}

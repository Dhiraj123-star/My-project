#include<iostream>
using   namespace std;

class A{

    public:
     void display(){
        cout<<"This is class A";

    }
};

class B{
    public:
    void display(){
        cout<<"This is class B";
    }
};

class C:A,B{ //C inherits A and B
    
};

int main(int argc, char const *argv[])
{
    //C obj ;

    //obj.display();
    return 0;
}

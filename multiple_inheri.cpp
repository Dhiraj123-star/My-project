//another example of multiple inheritance with some ambiguity
#include<iostream>
using namespace std;
class myclass{
    public:
    void display(){
        cout<<"This is the first base class function"<<endl;

    }

};
class yourclass{
    public:
    void display(){
        cout<<"this is overriden method "<<endl;
    }
};
class ourclass :public myclass,public yourclass{
    //blank 
};
int main(int argc, char const *argv[])
{
    //creating object
    ourclass obj1;
    // obj1.display(); it will throws error because it creates ambiguity to 
    //the complier which method will be called
    
    //this can be resoved  by following methods
    
    obj1.myclass::display();  //it will called first base class method
    obj1.yourclass::display(); //it will called second base class method


    return 0;
}


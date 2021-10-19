//multilevel inheritance in c++
#include<iostream>
using namespace std;
class class1{
    public :
    void showme(){
        cout<<"this is the base class function"<<endl;
    }
};
class class2:public class1{
    public :
    void showYou(){
        cout<<"This is second base class function"<<endl;

    }
};
class class3:public class2{
    public:
    void showUs(){
        cout<<"this is third class function"<<endl;

    }
};
main(){
    //creating object
    class3 c1;
    //calling methods 
    c1.showme();
    c1.showUs();
    c1.showYou();
}

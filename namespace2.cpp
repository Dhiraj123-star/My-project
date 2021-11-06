#include<iostream>
using namespace std;

namespace first{
    void display(){
        cout<<"This is the first namespace"<<endl;
    }
}
namespace second{
    void display(){
        cout<<"This is the second namespace "<<endl;
    }
}
//using  keyword to access the function inside the namespace

using namespace first;

int main(){

 display();

    return 0;

}
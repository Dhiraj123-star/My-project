//function overloading example
#include<iostream>
using namespace std;
void display(int val1,double val2){  //first function with two different parameters
        cout<<"Int: "<<val1<<" double:  "<<val2<<endl;

    }
    void display(int val1){  //second function with same name but single parameter
        cout<<"Int: "<<val1<<endl;
            }
    void display(double val2){ //third function with same name with single parameter but different type
        cout<<"Double: "<<val2<<endl;
    }
int main(){
    int var1=12;
    double var2=90.3;
    //calling first display()
    display(var1,var2);
    //calling second display()
    display(var1);
    //calling third display()
    display(var2);
    
    cout<<"Thanks for using C++ programming Language :)"<<endl;


    return 0;

}
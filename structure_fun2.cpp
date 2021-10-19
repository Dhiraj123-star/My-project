//structure and its function
#include<iostream>
using namespace std;
struct mystructure{
    char name[30];
    int age;
    float salary;
};

mystructure setdata(mystructure);
void displayData(mystructure);

int main(int argc, char const *argv[])
{
    mystructure s1;
    s1=setdata(s1);
    displayData(s1);
    return 0;
}

mystructure setdata(mystructure s1){
    cout<<"Enter Your name: "<<endl;
    cin.get(s1.name,30);
    cout<<"Enter Your age: "<<endl;
    cin>>s1.age;
    cout<<"Enter your salary: "<<endl;
    cin>>s1.salary;
    return s1;
} 
void displayData(mystructure s1){
    cout<<"Displaying details: "<<endl;
    cout<<"The name is: "<<s1.name<<endl;
    cout<<"The age is: "<<s1.age<<endl;;
    cout<<"The salary is: "<<s1.salary;
}
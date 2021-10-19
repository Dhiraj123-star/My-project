//structure example in c++
#include<iostream>
using namespace std;
struct Person{
    char name[50];
    int age;
    float salary;

};
int main(int argc, char const *argv[])
{
    Person p1;
    cout<<"Enter Your name: "<<endl;
    cin.get(p1.name,50);
    cout<<"Enter your age: "<<endl;
    cin>>p1.age;
    cout<<"Enter your salary: "<<endl;
    cin>>p1.salary;

    cout<<"\n Displaying information "<<endl;
    cout<<"Name : "<<p1.name<<endl;
    cout<<"Age: "<<p1.age<<endl;
    cout<<"Salary : "<<p1.salary<<endl;
    cout<<"Thanks for using c++ "<<endl;

    

    return 0;
}

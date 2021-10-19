//structure with function example
#include<iostream>
using namespace std;
struct Person{
    char name[50];
    int age;
    float salary;
};
void display(Person); //function declaration
int main(int argc, char const *argv[])
{
    Person p;
    cout<<"Enter your name"<<endl;
    cin.get(p.name,50);
    cout<<"Enter your age:"<<endl;
    cin>>p.age;
    cout<<"Enter your salary:"<<endl;
    cin>>p.salary;
    display(p); //function call with structure as an argument
    return 0;
}
void display(Person p){
    cout<<"Displaying details: "<<endl;
    cout<<"the name of person: "<<p.name<<endl;
    cout<<"the age of person "<<p.age<<endl;
    cout<<"the salary of person "<<p.salary<<endl;

    
}

#include<iostream>
#include<queue>
using namespace std;

int main(int argc, char const *argv[])
{
    
    priority_queue <string> p;

    priority_queue <string> r;

    //adding element into the p

    p.push("Aman");

    p.push("Yasweer");

    p.push("Dhiraj");

    p.push("Komal");

    //adding element into the q

    r.push("Ramesh");

    r.push("Pratham");

    r.push("Amresh");

    r.push("Gajendra");

    //swap () function

    p.swap(r);


    cout<<"The elements in the P are: "<<endl;

    while(!p.empty()){
        cout<<p.top()<<endl;

        p.pop();

    }
cout<<"The elements in the R are: "<<endl;

while(!r.empty()){
    cout<<r.top()<<endl;

    r.pop();

}

cout<<"The top of the element in r is: "<<r.top()<<endl;
    
    return 0;
}

//sum program in cpp
#include<iostream>
using namespace std;
class sample{
    int a,b,c;
    public:
    void getdata(int,int);
    void sum();
    void putdata();

};

void sample::getdata(int i,int j){
    a=i;
    b=j;

}
void sample::sum(){
    c=a+b;

}
void sample::putdata(){
    cout<<"The sum is:"<<c<<endl;

}
int main(int argc, char const *argv[])
{
    //creating object
    sample s1;
    s1.getdata(12,38);
    s1.sum();
    s1.putdata();

    return 0;
}

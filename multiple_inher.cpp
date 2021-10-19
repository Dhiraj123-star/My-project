//multiple inheritance in c++
#include<iostream>
using namespace std;
class science{
    public:
    science(){
        cout<<"this is science class "<<endl;
    }
};
class biology{
    public:
    biology(){
        cout<<"This is the biology class "<<endl;

    }
};
class medical : public biology,public science{
    public:
    medical(){
        cout<<"This is medical class "<<endl;
    }
};
int main(int argc, char const *argv[])
{
   //creating object
   medical m1; /*this will call all the constructors of 
   its base class because it is derived from them */
    return 0;
}

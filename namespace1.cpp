#include<iostream>
using namespace std;

namespace first{
    void sayhello(){
        cout<<"Hello First namespace"<<endl;

    }
}

namespace second{
    void sayhello(){
        cout<<"Hello second namespace"<<endl;
    }
}

int main(int argc, char const *argv[])
{
    
    first::sayhello();

    second::sayhello();
    
    return 0;
}

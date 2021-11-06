//simple example of signal handling using signal() function
#include<iostream>
#include<csignal>

using namespace std;

sig_atomic_t signalled =0;

void handler(int sig){

    signalled =1;
}

int main(int argc, char const *argv[])
{
    signal(SIGINT,handler);

    raise(SIGINT);
    
    if (signalled){
        cout<<"Signal is handled"<<endl;
    }
    else{
        cout<<"Signal is not handled"<<endl;
        
    }

    return 0;
}

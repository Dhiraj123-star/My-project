//signal handling using raise() function
#include<iostream>
#include <csignal>

using namespace std;

sig_atomic_t sig_value =0;

void handler(int sig){

    sig_value =sig;
}

int main(int argc, char const *argv[])
{
    signal(SIGABRT,handler);

    cout<<"Before signal handler is called: "<<endl;
    cout<<"Signal= "<<sig_value<<endl;

    raise(SIGABRT);
    cout<<"After signal handler is called: "<<endl;
    cout<<"Signal= "<<sig_value<<endl;
    
    return 0;
}

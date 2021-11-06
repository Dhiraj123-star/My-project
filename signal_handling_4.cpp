//signal handling program when SIGINT is passed to the raise() function
#include<iostream>

#include<csignal>

using namespace std;

sig_atomic_t value=0;

void handle(int signal_){

    value = signal_;
}

int main(int argc, char const *argv[])
{
    signal(SIGINT,handle);

    cout<<"Before called Signal: "<<value<<endl;
    raise(SIGINT);
    cout<<"After called signal: "<<value<<endl;
    
    
    return 0;
}

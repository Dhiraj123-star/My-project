//signal handling example 
# include<iostream>
#include<csignal>

using namespace std;

namespace{

    volatile sig_atomic_t gSignalStatus;

}

void signal_handler(int signal){

    gSignalStatus =signal;
}
int main(int argc, char const *argv[])
{
    //install a signal handler

    signal(SIGINT,signal_handler);
    

    cout<<"Signal value: "<<gSignalStatus<<endl;
    cout<<"Sending signal: "<<SIGINT<<endl;

    raise(SIGINT);

    cout<<"Signal value: "<<gSignalStatus<<endl;

    return 0;
}

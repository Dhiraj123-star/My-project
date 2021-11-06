//signal handling when SIGFPE is passed

#include<iostream>
#include<csignal>

using namespace std;

sig_atomic_t s_value =0; //this is default value 

void signal(int signal){

    s_value=signal;
}
int main(int argc, char const *argv[])
{
    signal(SIGFPE,signal);

    cout<<"Before calling signal: "<<s_value<<endl;

    raise(SIGFPE);

    cout<<"After called signal: "<<s_value<<endl;

    return 0;
}

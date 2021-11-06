//signal handling using SIGTERM 

#include<iostream>
#include<csignal>

using namespace std;

sig_atomic_t s_value =0;

void handle(int signal){
    s_value =signal;
}

int main(int argc, char const *argv[])
{

    signal(SIGTERM,handle);

    cout<<"Before the Signal: "<<s_value<<endl;

    raise(SIGTERM);


    cout<<"After the signal: "<<s_value<<endl;

    
    return 0;
}

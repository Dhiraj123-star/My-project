//signal handling using SIGSEGV 
# include<iostream>
#include<csignal>

using namespace std;

sig_atomic_t s_value =0;

void handle(int signal){
    s_value=signal;

}

int main(int argc, char const *argv[])
{
    signal(SIGSEGV,handle);

    cout<<"Before called signal: "<<s_value<<endl;
    raise(SIGSEGV);

    cout<<"After called signal: "<<s_value<<endl;
    




    return 0;
}

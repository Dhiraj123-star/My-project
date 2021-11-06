
#include<iostream>
#include<Bits.h>
using namespace std;

//function converts character array to string and return it

string convertToString(char* array,int size){
    int i;

    string result_string =" ";
    for(int i=0; i<size; i++){
        result_string = result_string + array[i];
    }
    return result_string;
}
int main(int argc, char const *argv[])
{
    char array[]={'c','o','d','i','n','g'};
    int size = sizeof(array)/sizeof(char);

    string result_string = convertToString(array,size);

    cout<<result_string<<endl;


    return 0;
}


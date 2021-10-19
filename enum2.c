//enum with custom values
#include<stdio.h>

enum myvalue{

    //enum with custom values

    Python=1,
    Java=10,
    Go=2,
    Scala=4,
    C=9,
    JavaScript=3

};

int main(int argc, char const *argv[])
{

 enum myvalue  lang;
 lang= Go;
 printf("the rank of programming language is %d",lang);

 printf("The size of enum variable is:%d", sizeof(lang)); //returns 4

    return 0;
}

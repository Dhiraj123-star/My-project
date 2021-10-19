//enum example in C
#include<stdio.h>

enum Weeks{
    sunday, // by default it starts by 0
    monday,
    tuesday,
    wednesday,
    thursday,
    friday,
    saturday
};
int main(int argc, char const *argv[])

{
    enum Weeks myday;
    myday = saturday;

    printf("The day value is %d",myday);


    
    return 0;
}

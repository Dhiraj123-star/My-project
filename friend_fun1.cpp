//friend function example
#include<iostream>
using namespace std;
class Distance {
    private:
        int meter;
        
        // friend function
        friend int addTen(Distance);

    public:
        Distance() : meter(1) {}
        
};

// friend function definition
int addTen(Distance d) {

    //accessing private members from the friend function
    d.meter += 10;
    return d.meter;
}

int main() {
    Distance D;
    cout << "Distance: " << addTen(D);
    return 0;
}
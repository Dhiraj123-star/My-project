
#include<iostream>
#include<map>
#include<iterator>

using namespace std;
int main(int argc, char const *argv[])
{
    //empty map constructor

    map<char , int> alpha;

    alpha.insert(pair<char,int>('A',1));
    alpha.insert(pair<char,int>('B',2));
    alpha.insert(pair<char,int>('C',3));
    alpha.insert(pair<char,int>('D',4));
    alpha.insert(pair<char,int>('E',5));
    alpha.insert(pair<char,int>('F',6));
    alpha.insert(pair<char,int>('G',7));
    alpha.insert(pair<char,int>('H',8));
    alpha.insert(pair<char,int>('I',9));
    alpha.insert(pair<char,int>('J',10));
    alpha.insert(pair<char,int>('K',11));
    alpha.insert(pair<char,int>('L',12));
    alpha.insert(pair<char,int>('M',13));
    alpha.insert(pair<char,int>('N',14));
    alpha.insert(pair<char,int>('O',15));
    alpha.insert(pair<char,int>('P',16));
    alpha.insert(pair<char,int>('Q',17));
    alpha.insert(pair<char,int>('R',18));
    alpha.insert(pair<char,int>('S',19));
    alpha.insert(pair<char,int>('T',20));
    alpha.insert(pair<char,int>('U',21));
    alpha.insert(pair<char,int>('V',22));
    alpha.insert(pair<char,int>('W',23));
    alpha.insert(pair<char,int>('X',24));
    alpha.insert(pair<char,int>('Y',25));
    alpha.insert(pair<char,int>('Z',26));
    
//taking input from the user 
    string name;
    cout<<"Enter your name in uppercase:  ";
    cin>>name;

    //iterate through the character of the name

    for (int i=0; i<name.length(); i++){

//iterate through the map elements 
        for(auto it=alpha.begin(); it!=alpha.end(); ++it){

//matching the map keys with character of name
        if(name[i]==it->first){
//printing the value of matched keys 
            cout<<it->second<<endl;
        }
    }
}

  
  
return 0;
}
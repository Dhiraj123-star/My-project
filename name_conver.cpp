#include<iostream>
#include<map>
using namespace std;
int main(int argc, char const *argv[])
{

  map <int ,string> programming_lang;


  programming_lang.insert(pair<int,string>(1,"Python"));
  //inserting using index notation
  programming_lang[2]="Java";

  programming_lang.insert(pair<int,string>(3,"Julia"));
  programming_lang.insert(pair<int,string>(4,"C++"));
  programming_lang.insert(pair<int,string>(5,"PHP"));

  programming_lang[6]="JavaScript";
  programming_lang[7]="C";


  //find out any value

  cout<<"Programming_lang[4]: "<<programming_lang[4]<<endl;

//find out the size

cout<<"The size of the programming language :"<<programming_lang.size()<<endl;

//iterating through the map
//auto itr is just a variable name of iteration type

for(auto itr=programming_lang.begin(); itr!=programming_lang.end();++itr){
    cout<<itr->first <<" : "<<itr->second<<endl;

}




    return 0;
}

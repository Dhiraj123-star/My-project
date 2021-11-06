#include<iostream>
#include<map>
#include<string>

using namespace std;

int main(int argc, char const *argv[])
{
    multimap<string,string> m ={
        {"india","new delhi"},
        {"india","bhiwadi"},
        {"india","Hyderabad"},
        {"india","noida"}
    };

    //inserting new element

    m.insert(pair<string,string>("india","Lucknow"));

    m.insert(pair<string,string>("india","Allahabad"));

    cout<<"Size of the map is: "<<m.size()<<endl;

    cout<<"Elements in map is: "<<endl;

    for(multimap<string,string>::iterator itr = m.begin(); itr!=m.end(); ++itr)
{
    cout<<(*itr).first<<":"<<(*itr).second<<endl;

}
    
    return 0;
}

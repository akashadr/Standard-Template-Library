#include <iostream>
#include <list>
using namespace std;


int main()
{
    list<int> d={1,2,3};
    
    d.push_back(4);
    d.push_front(0);
    
    for(int i:d)
      cout<<i<<" ";
    cout<<endl;

    d.pop_back();
    
    for(int i:d)
      cout<<i<<" ";
    cout<<endl;
    
    d.pop_front();
    
    for(int i:d)
      cout<<i<<" ";
    cout<<endl;
    
    cout<<d.front()<<endl;
    cout<<d.back()<<endl;
    
    //cout<<"Iteam at 1th Index: "<<d.at(1)<<endl;
    
    cout<<d.size()<<endl;
    cout<<d.empty()<<endl;
    
    d.erase(d.begin(),d.end());
    
    for(int i:d)
      cout<<i<<" ";
    cout<<endl;
    
    cout<<d.size()<<endl;
    cout<<d.empty()<<endl;
    
}
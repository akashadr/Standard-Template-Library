#include <iostream>
#include <vector>
using namespace std;


int main()
{
    vector<int> v;
    
    cout<<v.capacity()<<endl;
    
    v.push_back(1);
    
    cout<<v.capacity()<<endl;
    
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    
    cout<<v.capacity()<<endl;
    cout<<v.size()<<endl;
    
    cout<<v.front()<<endl;
    cout<<v.back()<<endl;
    
    for(int i:v)
       cout<<i<<" ";
    cout<<endl;
    
    v.pop_back();
    
    cout<<v.capacity()<<endl;
    cout<<v.size()<<endl;
    
    for(int i:v)
       cout<<i<<" ";
    cout<<endl;
    
    cout<<v.empty()<<endl;
    
    v.clear();
    
    cout<<v.capacity()<<endl;
    cout<<v.size()<<endl;
    
    for(int i:v)
       cout<<i<<" ";
    cout<<endl;
    
    cout<<v.empty()<<endl;
    
    cout<<"New Vector"<<endl;
    
    vector<int> x(5,1);
    
    cout<<x.capacity()<<endl;
    cout<<x.size()<<endl;
    
    for(int i:x)
       cout<<i<<" ";
    cout<<endl;
    
    cout<<"Inherited Vector"<<endl;
    
    vector<int> y(x);
    
    cout<<y.capacity()<<endl;
    cout<<y.size()<<endl;
    
    y.pop_back();
    
    cout<<y.capacity()<<endl;
    cout<<y.size()<<endl;
    
    for(int i:y)
       cout<<i<<" ";
    cout<<endl;
    
    vector<int> z(1,5);
    for(int i:z)
       cout<<i<<" ";
    cout<<endl;
    
    z.push_back(7);
    for(int i:z)
       cout<<i<<" ";
    cout<<endl;
    
}
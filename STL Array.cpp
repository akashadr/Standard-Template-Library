#include <iostream>
#include <array>
using namespace std;


int main()
{
    array<int,5> arr;
    arr={1,2,3,4,5};
    
    for(int i=0;i<arr.size();i++)
      cout<<arr[i]<<endl;
      
    cout<<"Item at 3rd Index: "<<arr.at(3)<<endl;
    cout<<arr.empty()<<endl;
    cout<<arr.front()<<endl;
    cout<<arr.back()<<endl;
}
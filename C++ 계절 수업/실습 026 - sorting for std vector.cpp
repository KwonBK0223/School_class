#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> v;
    int SIZE;
    cin >> SIZE;
    int a;

    for(int i=0 ; i< SIZE; i++)
    {
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end());

    for(int i = 0 ; i< SIZE; i++)
        cout << v[i] <<" ";

}
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int a;
    vector<int> v;
    while(1){
        cin >> a;
        if (cin.eof()) break;
        v.push_back(a);
    }
    auto min = min_element(v.begin(),v.end());
    auto max = max_element(v.begin(),v.end());
    cout << v.size() << " " << *min << " " << *max << endl;
}
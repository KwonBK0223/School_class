#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> v;
    int SIZE;
    cin >> SIZE;
    int a;

    for(int i = 0; i<SIZE; i++){
        cin >> a;
        v.push_back(a);
    }
    int M,O;
    cin >> M;
    v.erase(v.begin()+M);
    cin >> O;
    v.erase(remove(v.begin(),v.end(), O),v.end());
    cout << v.size() << endl;
    for (auto i :v) cout << i << " ";
}
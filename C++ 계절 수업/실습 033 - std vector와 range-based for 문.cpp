#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> v;
    int SIZE;
    cin >> SIZE;
    int a;
    int sum = 0;
    for(int i =0; i<SIZE; i++){
        cin >> a;
        v.push_back(a);
    }
    for(int i=0;i<SIZE;i++){

        sum = sum+v[i];
    }
    cout << sum << endl;

}
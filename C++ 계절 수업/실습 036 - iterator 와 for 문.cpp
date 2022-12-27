#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main(){
    vector<int> vec;
    istream_iterator<int>cin_iter(cin);
    istream_iterator<int>eos;
    copy(cin_iter, eos, back_inserter(vec));
    ostream_iterator<int>cout_iter(cout," ");
    sort(vec.begin(), vec.end());
    copy(vec.begin(),vec.end(),cout_iter);
}
#include <algorithm>
#include <iterator>
#include <numeric>
#include <iostream>
#include <vector>

int main(){
    int N,X;
    std::cin >> N>>X;
    std::vector<double> vec;
    std::generate_n(std::back_inserter(vec), N, [] () {return *(std::istream_iterator<double>{std::cin}); });
    copy_if (vec.begin(), vec.end(), std::ostream_iterator<int>(std::cout, " "), [=](int x){return X > x;});


}
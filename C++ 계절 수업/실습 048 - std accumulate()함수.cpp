#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <numeric>
#include <iterator>

int main(){
    int N; std::cin >> N;

    std::vector<double> vec;

    std::generate_n(std::back_inserter(vec), N, [] () { return *(std::istream_iterator<double>{std::cin}); });
    double sum = accumulate(vec.begin(), vec.end(), 0.0);
    std::cout<<sum;
}
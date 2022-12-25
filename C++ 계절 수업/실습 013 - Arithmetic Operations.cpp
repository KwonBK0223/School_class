/* 정수로 입력 받아서 실수로 저장기
 * 힌트
 * #include <iomanip>   // you need to include this header file
std::cout << std::fixed << std::setprecision( 2 ) <<  5/3;   // print 1.67 on stdout
 * */
#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float x,y;
    cout<<" ";
    cin>>x;
    cin>>y;

    cout<<fixed<<setprecision(2)<<x<<"+"<<y<<"="<<x+y<<endl;
    cout<<fixed<<setprecision(2)<<x<<"-"<<y<<"="<<x-y<<endl;
    cout<<fixed<<setprecision(2)<<x<<"*"<<y<<"="<<x*y<<endl;
    cout<<fixed<<setprecision(2)<<x<<"/"<<y<<"="<<x/y<<endl;

    return 0;
}

/* 다음과 같이 동작하는 프로그램을 작성하시오.
 * 1.int long float double 의 타입 이름을 문자열로서 입력 받아서 각 타입이 표현할 수 있는 최대값과 최소값을 출력한다
 * 2.타입이름이 입력되는 동안 반복적으로 수행되면 "quit" 문자열이 입력되면 반복문은 종료된다.
 * 3.반복문이 종료되면 각 타입 별로 실제로 입력된 횟수를 출력한다.
 * 4.대소문자를 구분하지 않는다.
 *
 * 제약조건 입출력에는 cin, cout 사용
 *        문자열은 string 사용
 *        numeric_limits<T>를 이용하시오
 *        정의되지 않은 문자열이 들어오는 경우 Invalid Command 를 출력하시오
 */

#include <iostream>
#include <algorithm>
#include <limits>

using namespace std;

int main(){
    string cmd;
    int Int = 0, Long = 0, Short = 0, Float = 0, Double = 0;
    while(1){
        cin >> cmd;
        transform(begin(cmd), end(cmd), begin(cmd), [](unsigned char c) {return tolower(c);});
        if (cmd == "int"){
            Int = Int+1;
            cout << numeric_limits<int>::max() << " " << numeric_limits<int>::min() <<endl;
        }
        else if (cmd == "long") {
            Long = Long+1;
            cout << numeric_limits<long>::max() << " " << numeric_limits<long>::min() <<endl;
        }
        else if (cmd == "short") {
            Short = Short+1;
            cout << numeric_limits<short>::max() << " " << numeric_limits<short>::min() <<endl;
        }
        else if (cmd == "float") {
            Float = Float+1;
            cout << numeric_limits<float>::max() << " " << numeric_limits<float>::min() <<endl;
        }
        else if (cmd == "double") {
            Double = Double+1;
            cout << numeric_limits<double>::max() << " " << numeric_limits<double>::min() <<endl;
        }
        else if (cmd == "quit")
            break;
        else
            cout << "Invalid Command" << endl;
    }
    cout << "=== the number of types ===" << endl;
    cout << "int : " << Int << endl;
    cout << "long : " << Long << endl;
    cout << "float : " << Float << endl;
    cout << "double : " << Double << endl;

    return 0;
}
/* 표준입력(stdin)에서 입력을 읽어서, 표준출력(stdout)으로 원하는 값을 출력하기
 * 설명
 * C++에서는 cin 을 사용하여 공백으로 구분된 단일 입력 값을 읽을 수 있습니다. 예를 들어, 다음 변수를 선언한다고 가정해 보겠습니다.
string s;
int n;
cin 을 사용하여 stdin 으로부터 "hello 10" 입력을 읽으려고 합니다. 그러면 다음 코드로 수행할 수 있습니다.
cin >> s >> n;
이것은 stdin 에서 첫 번째 단어인 "hello"를 읽고, string 타입 s 변수에 그 값을 저장한 다음, stdin 에서 두 번째 단어(10) 을 읽고, int 타입 n 변수에 그 값을 저장합니다.
두 값을 공백으로 구분하여 stdout 에 인쇄하려면 다음 코드를 작성합니다.
cout << s << " " << n << endl;
이 코드는 string 의 내용 ("hello"), 공백 하나 (" "), 정수 (10)을 stdout 에 출력합니다. endl 을 사용하여 엔터(개행문자, \n) 을 추가하였습니다.
화면에 다음과 같이 출력됩니다.
hello 10
*/
#include <iostream>
using namespace std;
int main(){
    int x,y,z;
    int sum;
    cout<<" ";
    cin>>x;
    cout<<" ";
    cin>>y;
    cout<<" ";
    cin>>z;
    sum=x+y+z;
    cout<<""<<sum<<endl;
    return 0;
}
#include <iostream>
#include <string>
using namespace std;

void println(string& str){

    cout << str;
}

int main(){
    string str = "hello, world!";
    println(str);
    for(int i =0;i<3;i++){
        cout<< "\n";
        println(str);

    }
}
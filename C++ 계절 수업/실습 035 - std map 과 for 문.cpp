#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    int N ;
    cin >> N;
    map<string,string>phonebook;
    string name, pnum;
    for (int i = 0 ; i< N; i++){
        cin >> name >> pnum;
        phonebook[name]=pnum;
    }
    string s;
    while(cin>>s){
        if (s == "QUIT") break;
        auto found = phonebook.find(s);
        if(found != phonebook.end())
            cout << found->second << endl;
        else
            cout << "NOT FOUND"<< endl;
    }
}
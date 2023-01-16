#include <iostream>
#include <regex>
#include <map>
#include <algorithm>
using namespace std;
int main(){
    string s1;
    map<string,size_t> words;
    int n = 1;
    while(cin>>s1&&s1!="^"){
        transform(s1.begin(),s1.end(),s1.begin(),::tolower);
        auto s1f {regex_replace(s1,regex("[.|,|:|;| ]"), "")};
        auto sear=words.find(s1f);
        if (sear !=words.end())
            words[s1f]++;
        else
            words[s1f] =n;
    }
    cout << "words:"<<words.size()<<endl;
    string s2;
    while(cin>>s2&&s2!="QUIT"){
        transform(s2.begin(),s2.end(),s2.begin(),::tolower);
        auto s2f = words.find(s2);
        if(s2f==words.end()){
            cout<<s2<<":"<<0<<endl;
        }
        else
            cout<<s2<<":"<<words[s2]<<endl;
    }
    cout<<"Bye!";
}
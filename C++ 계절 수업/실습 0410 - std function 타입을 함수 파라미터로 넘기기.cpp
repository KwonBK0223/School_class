#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <ostream>
#include <functional>
#include "Champion.h"

using namespace std;

int main(){
    vector<Champion> ch = createChampion();
    string s;
    int n;
    cin >>s;
    string s1 = s.substr(0,6);
    string s2 = s.substr(7);
    if(s1=="health"){
        stringstream ss(s2);
        ss>>n;
        function<bool(Champion)> condition1=[&n](Champion c){return c.health>n;};
        auto result1 = findChampionWithCondition(ch,condition1);
        printChampion(result1);
    }
    else if (s1=="attack"){
        stringstream ss(s2);
        ss>>n;
        function<bool(Champion)> condition2=[&n](Champion c){return c.attack>n;};
        auto result2 = findChampionWithCondition(ch,condition2);
        printChampion(result2);
    }
    else
        cout<<"Unknown";
}

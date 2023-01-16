#include <iostream>
#include <map>
#include "Person.h"

using namespace std;
int main(){
  int n; string q;
  cin>>n;
  map<string, Person> persons;
  for(int i =0;i<n;i++){
    string s;
    string num;
    cin >> s>>num;
    persons.insert({s,{s,num}});
  }
  while(cin>>q){
    string s,n;
    if(q=="ADD"){
      cin>>s>>n;
      persons.insert({s,{s,n}});
    }
    else if(q=="DEL"){
      cin>>s;
      persons.erase(s);
    }
    else if (q=="MOD"){
      cin>>s>>n;
      auto find_it =persons.find(s);
      find_it->second.modifyNumber(n);
    }
    else if (q=="FIN"){
      cin>>s;
      auto find_it = persons.find(s);
      find_it->second.print();
    }
    else break;
  }
  for (const auto& d:persons) d.second.print();
  return 0;
}
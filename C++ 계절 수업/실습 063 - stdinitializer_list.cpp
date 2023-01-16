#include <iostream>
#include <string>
#include <map>
#include <initializer_list>
#include <utility>
using namespace std;

class Phonebook {
  map<string, int> contacts;
 public:
  Phonebook(initializer_list <pair<string, int>> lst) {
    for(auto& i:lst)
      contacts.insert(i);
  }
  void print() const {
    for(auto& i:contacts)
      cout<<i.first<<" "<<i.second<<endl;
  }
};



int main() {
  Phonebook p = {{"Kim", 24}, {"Lee", 21}};
  p.print();
  return 0;
}
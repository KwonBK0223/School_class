#include <string>

class Person{
 public :
  Person(std::string name, std::string number);
  void modifyNumber(std::string number);
  void print() const;
 private:
  std::string name;
  std::string number;

};
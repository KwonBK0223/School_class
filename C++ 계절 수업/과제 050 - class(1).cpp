#include <iostream>
#include "student.h"
using namespace std;

std::pair<std::string, Student> Student::createFromKeyboard() {
  string id, name;
  double gpa;
  cin>>id>>name>>gpa;
  Student st{id,name,gpa};
  return {id,st};
}
void Student::modifyGPA(double gpa) {
  this->_gpa = gpa;
}
void Student::print() const {
  cout<<this->_id<<" "<<this->_name<<" "<<this->_gpa<<endl;
}
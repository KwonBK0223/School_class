#include "student.h"
#include <iostream>
#include <iomanip>
using namespace std;
shared_ptr<Student> getStudent(){
  string name;
  float gpa;
  cin>>name>>gpa;
  shared_ptr<Student> st(new Student(name,gpa));
  return st;
}
void print(const vector<shared_ptr<Student>>& students){
  for(auto& i:students)
    cout<<fixed<<setprecision(1)<<"Name: "<<i->name<<", GPA: "<<i->gpa<<endl;
}
float getAverage(const vector<shared_ptr<Student>> &students, int no){
  float tot,avg;
  for(auto& i:students)
    tot+=i->gpa;
  avg = tot/no;
  return avg;
}
void plusGPA(vector<shared_ptr<Student>>& students, float bonus){
  for(auto& i:students)
    i->gpa = i->gpa+1;
}
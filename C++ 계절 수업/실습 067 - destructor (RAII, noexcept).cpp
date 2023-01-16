#include <cstring>
#include <iostream>
#include "String.h"

String::String() {
  s = new char [1];
  s[0] = '\0';
  len = 0;
}
String::String(const char *str){
  if(str){
    s= new char[strlen(str)+1];
    len = strlen(str);
    strcpy(s,str);
  }
  else{
    s = new char [1];
    len = 0;
    s[0] = '\0';
  }
}
String::String(const String& str) : s(new char[str.len +1]), len(str.len){
  for(int i = 0; i < str.len ;i++)
    s[i]=str.s[i];
}
String& String::operator=(const String& str){
  if(this == &str)
    return *this;
  len = str.len;
  for(int i = 0;i<str.len;i++)
    s[i]=str.s[i];
  return *this;
}
String::~String() {
  delete [] s;
  std::cout<<"Destructor"<<std::endl;
}
const char* String::data() const{
  return s;
}
char& String::at(size_t t){
  return s[t];
}
void String::print(const char *str) const{
  std::cout<<str<<": ";
  for(int i =0;i<len;i++)
    std::cout<<s[i];
  std::cout<<", size"<<size()<<std::endl;
}
size_t String::size() const{
  return len;
}
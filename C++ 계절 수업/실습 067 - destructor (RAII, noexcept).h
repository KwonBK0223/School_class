//
// Created by kbk on 2023-01-16.
//

#ifndef UNTITLED7__STRING_H_
#define UNTITLED7__STRING_H_
#include <stddef.h>
class String{
 public:
  String();
  String(const char* str);
  String(const String& str);
  String& operator=(const String& str);
  ~String();
  const char* data() const;
  char& at(size_t);
  size_t size() const;
  void print(const char* str="") const;
 private:
  int len;
  char* s;
};
#endif //UNTITLED7__STRING_H_

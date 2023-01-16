//
// Created by kbk on 2023-01-16.
//

#ifndef UNTITLED__ARRAY_H_
#define UNTITLED__ARRAY_H_
#include <stddef.h>
class Array {
 public:
  Array(std::initializer_list<int> d,size_t size);
  Array(const Array& arr);
  Array& operator =(const Array& arr);
  ~Array();
  int& at(size_t size);
  std::string print() const;
 private:
  int* data = nullptr;
  size_t _size = 0;
};

#endif //UNTITLED__ARRAY_H_

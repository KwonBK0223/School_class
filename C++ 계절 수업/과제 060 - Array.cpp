#include <iostream>
#include <sstream>
#include "Array.h"

Array::Array(std::initializer_list<int> d, size_t size) {
  data = new int[size];
  _size = size;
  int cnt = 0;
  for(auto& i:d){
    data[cnt] = i;
    ++cnt;
  }
}
Array::Array(const Array& arr):data(new int[arr._size]),_size(arr._size){
  for(int i =0;i<arr._size;i++)
    data[i]=arr.data[i];
}
Array &Array::operator=(const Array &arr) {
  if(this == &arr)
    return *this;
  _size = arr._size;
  for (int i =0;i<arr._size;i++)
    data[i]=arr.data[i];
  return *this;
}
int& Array::at(size_t size) {
  std::cout<<"copy constructor"<<std::endl;
  if(_size!=0 && 0<=size && size<_size)
    return data[size];
  throw std::out_of_range("out of range at index: "+std::to_string(size)+", but the length of String is"+std::to_string(_size));
}
std::string Array::print() const{
  std::stringstream ss;
  for(int i = 0;i<this->_size;i++)
    ss<<this->data[i]<<" ";
  std::string str = ss.str();
  return str;
}
Array::~Array() {
  delete [] data;
}
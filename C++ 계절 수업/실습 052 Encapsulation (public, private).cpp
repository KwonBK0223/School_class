#include "Cell.h"

namespace PNU {
void Cell::setValue(double iVal) {
  number_value = iVal;
}
void Cell::setValue(std::string sVal) {
  string_value = sVal;
}
std::string Cell::toString() const {
  if(number_value !=0){
    std::string s = std::to_string(number_value);
    return s;
  }
  else
    return string_value;
}
template<> std::string Cell::getValue() const {return string_value;}
template<> double Cell::getValue() const {return number_value;}
std::ostream &operator<<(std::ostream &os,const Cell &c){
  os << c.toString();
  return os;
}
}
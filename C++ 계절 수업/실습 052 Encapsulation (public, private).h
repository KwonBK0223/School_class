
//
// Created by kbk on 2023-01-11.
//

#ifndef UNTITLED__CEL_H_
#define UNTITLED__CEL_H_
#include <iostream>
#include <string>
namespace PNU {
enum cell_type { number, str};
class Cell {
 public:
  void setValue(double iVal);
  void setValue(std::string sVal);

  template<typename T> T getValue() const;
  friend std::ostream &operator<<(std::ostream &os, const Cell &c);
 private:
  std::string toString() const;
  std::string string_value;
  double number_value=0;
};
template<> double Cell::getValue<double>() const;
template<> std::string Cell::getValue<std::string>() const;
}
#endif //UNTITLED__CEL_H_

#ifndef UNTITLED2__COMPLEX_H_
#define UNTITLED2__COMPLEX_H_
#include <iostream>
class complex {
 public:
  complex(double rr=0, double ii = 0):r(rr),i(ii) {}
  complex add(const complex& c) { return {r+c.r, i+c.i};};
  friend std::ostream& operator<<(std::ostream& os, const complex& c);
 private:
  double r{0}, i{0};
};
std::ostream& operator<<(std::ostream& os, const complex& c){
  std::cout << c.r << " + " << c.i << "i";
  return os;
}
#endif //UNTITLED2__COMPLEX_H_

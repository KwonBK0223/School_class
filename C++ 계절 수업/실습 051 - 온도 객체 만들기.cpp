#include <iomanip>
#include <string>
#include <iomanip>
#include "Temperature.h"

std::string Temperature::print() const {
  std::stringstream ss;
  ss << std::fixed << std::setprecision(1) << degree << (scale == CELSIUS ? " C": " F") << std::endl;
  return ss.str();
}
float Temperature::convert(SCALE scale){
  float d= degree;
  if(scale == CELSIUS)
    d = d*((float)9/5)+32;
  else
    d = (d-32)*((float)5/9);
  return d;
}

Temperature Temperature::add(Temperature t) const{
  float d;SCALE s;
  s = this ->scale;
  if(s!=t.scale)
    d=(this->degree)+ t.convert(t.scale);
  else
    d = this->degree + t.degree;
  return Temperature{d,s};
}

Temperature::Temperature(float degree, SCALE scale) {
  this->degree = degree;
  this->scale = scale;
}
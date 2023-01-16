//
// Created by kbk on 2023-01-16.
//

#ifndef UNTITLED3__VEHICLE_H_
#define UNTITLED3__VEHICLE_H_
#include <string>
class Vehicle {
 public:
  Vehicle() : name("Model Y LR"),range(511),hasFDS(false),batteryCapacity(85) {}
  Vehicle(std::string n, int r, bool fds, float bc) : name(n), range(r),hasFDS(fds),batteryCapacity(bc) {}
  Vehicle(std::string n, int r, float bc) : Vehicle(n,r,false,bc) {}
  void autoPilot(bool onOff);
  void runFDS() const;
  void displayEfficiency() const;
 private:
  std::string name;
  int range;
  bool hasFDS;
  float batteryCapacity;
};

#endif //UNTITLED3__VEHICLE_H_

#include <iostream>
#include <iomanip>
#include "Vehicle.h"

// your code here

void Vehicle::autoPilot(bool onOff){
  std::cout << "Auto-Pilot is " << (onOff ? "on!" : "off!") << std::endl;
}

void Vehicle::runFDS() const {
  if(hasFDS)
    std::cout << "Full Self-Driving!" << std::endl;
}

void Vehicle::displayEfficiency() const {
  std::cout << name << " Range: " << range << "km, Efficiency: " << std::setprecision(3) << range / batteryCapacity << "kWh/100km" << std::endl;
}
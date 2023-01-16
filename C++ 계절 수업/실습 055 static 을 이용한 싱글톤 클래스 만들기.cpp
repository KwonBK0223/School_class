#include "SharedPreferences.h"

SharedPreferences& SharedPreferences::getInstance() {
  static SharedPreferences sharedPreferences;
  return sharedPreferences;
}
void SharedPreferences::putInt(std::string key, int value) {}
int SharedPreferences::getInt(std::string key) {
  return 0;
}
size_t SharedPreferences::size() {
  return 0;
}
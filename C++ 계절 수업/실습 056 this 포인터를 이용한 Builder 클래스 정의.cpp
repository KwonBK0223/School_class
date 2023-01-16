#include "Notification.h"
#include <iostream>
#include <string>
#include <ctime>

std::ostream& operator << (std::ostream& os, const Notification& n){
  os << n.icon << " " << n.appName << " " ;
  int diff = (int)std::difftime(std::time(nullptr), n.timestamp) / (60 * 60 * 24);
  os <<  ((diff==0) ? "now" : std::to_string(diff) );
  os << ((diff==0) ? "" : " days" ) << std::endl;
  os << n.title << std::endl;
  os << n.text << std::endl;
  return os;
}
NotificationBuilder Notification::create(){
  NotificationBuilder b;
  return b;
}

NotificationBuilder& NotificationBuilder::setSmallIcon(int icon) {
  this->notification.icon = icon;
  return *this;
}

NotificationBuilder& NotificationBuilder::setContentTitle(std::string title) {
  this->notification.title= title;
  return *this;
}


NotificationBuilder& NotificationBuilder::setContentText(std::string text) {
  this->notification.text = text;
  return *this;
}


NotificationBuilder& NotificationBuilder::setPriority(int priority) {
  this->notification.priority = priority;
  return *this;
}


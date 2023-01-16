//
// Created by kbk on 2023-01-16.
//

#ifndef UNTITLED1__POINT_H_
#define UNTITLED1__POINT_H_

class Point {
 public:
  Point(double x =0, double y = 0): x(x), y(y) {}
  double getX() const {return x;}
  double getY() const {return y;}
 private:
  const double x,y;
};
#endif //UNTITLED1__POINT_H_

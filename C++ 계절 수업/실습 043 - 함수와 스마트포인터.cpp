#include "student.h"
#include <iostream>
#include <vector>
#include <memory>
#include <string>
using namespace std;

int main(){
    vector<unique_ptr<STUDENT>> vec;
    int n=0;
    int age;
    string name;
    cin >> n;
    for(int i =0;i<n;i++){
        cin >> name >> age;
        vec.push_back(createStudent(name,age));
        printStudentInfo(*vec[i]);
    }
}
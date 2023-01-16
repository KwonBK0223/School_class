#include "school.h"

#include "student.h"

#include <algorithm>

#include <iostream>

#include <map>

using namespace std;

enum Command { ADD, DELETE, PRINT, FIND, MODIFY, QUIT, INVALID };

Command getCommand(const string& command){
  if(command == "add")
    return ADD;
  else if(command == "delete")
    return DELETE;
  else if(command == "print")
    return PRINT;
  else if(command == "find")
    return FIND;
  else if(command == "modify")
    return MODIFY;
  else if(command == "quit")
    return QUIT;
  else
    return INVALID;
}



int main() {

  cout << "Set School Name : ";

  string schoolName; cin >> schoolName;

  School& school = School::getInstance(schoolName);



  while(true) {

    cout << "Enter Command: ";

    string cmd; cin >> cmd;

    transform(begin(cmd), end(cmd), begin(cmd), [](char& c){return tolower(c);});

    Command c = getCommand(cmd);

    switch(c) {
      case ADD:{
        cout<<"Enter id,name,gpa : ";
        auto st = Student::createFromKeyboard();
        auto id = st.first;
        school.addStudent(id,st);
        break;
      }
      case DELETE:{
        string id;
        cout<< "Enter id : ";
        cin>>id;
        school.deleteStudent(id);
        break;
      }
      case PRINT:
        school.print();
        break;
      case FIND:{
        string id;
        cout<<"Enter id : ";
        cin>> id;
        school.print(id);
        break;
      }
      case MODIFY:{
        string id; double gpa;
        cout<<"Enter id, gpa : ";
        cin>>id>>gpa;
        school.modifyStudentGPA(id,gpa);
        break;
      }
      case QUIT:
        return 0;
      case INVALID:
        break;

    }

  }

}
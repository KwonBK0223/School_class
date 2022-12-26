#include <iostream>
#include <string>

using namespace std;

enum TYPE {INT, LONG, FLOAT, DOUBLE};
TYPE getType(string type){
    if (type == "int")
        cout << "INT(0)";
    else if (type == "long")
        cout << "LONG(1)";
    else if (type == "float")
        cout << "FLOAT(2)";
    else
        cout << "DOUBLE(3)";
}

int main() {
    string str;
    cin >> str;
    TYPE type = getType(str);
    switch (type) {
        case INT:
            cout << "INT(" << type << ")" << endl;
            break;
        case LONG:
            cout << "LONG(" << type << ")" << endl;
            break;
        case FLOAT:
            cout << "FLOAT(" << type << ")" << endl;
            break;
        case DOUBLE:
            cout << "DOUBLE(" << type << ")" << endl;
            break;
    }
    return 0;
}

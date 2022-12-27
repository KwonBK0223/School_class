#include <iostream>
using namespace std;
enum Color {Red = 0, Green = 1 , Blue = 2};

int main(){
    int color;
    cin >> color;

    Color colorcode ;
    if (color == 0)
        colorcode = Red;
    else if (color == 1)
        colorcode = Green;
    else
        colorcode = Blue;

    switch (colorcode){
        case Red:
            cout<<"It's red light!"<<endl;
            break;
        case Green:
            cout<<"It's green light!"<<endl;
            break;
        case Blue:
            cout<<"It's blue light!"<<endl;
            break;
    }
}
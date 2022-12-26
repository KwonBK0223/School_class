#include "pointer.h"
#include <iostream>
using namespace std;
#include "pointer.h"

void update(int* a, int* b){
    int temp = *a;
    *a = *a+*b;
    *b = temp-*b;

    return ;
}

int main(){
    int a, b;
    int* pA = &a;
    int* pB = &b;

    cin >> *pA >> *pB;

    update(&a, &b);

    cout << a << endl;
    cout << b << endl;

}

/*
pointer.h

#ifndef HELLO_POINTER_H

#define HELLO_POINTER_H

void update(int* a, int* b);

#endif //HELLO_POINTER_H b*/

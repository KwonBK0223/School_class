#include <iostream>
using namespace std;

int main(){
    int SIZE = 0;
    int i=0;
    cin >> SIZE;
    int* arr = new int[SIZE];
    while (i<SIZE){
        cin >> *(arr+i);
        i++;
    }
    cin >> i;
    cout << arr[arr[i]] << endl;

    delete [] arr;
}
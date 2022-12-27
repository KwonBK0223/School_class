#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int SIZE = 0;
    int i =0;
    cin >> SIZE;
    int *arr = new int[SIZE];
    while (i<SIZE){
        cin >> arr[i];
        i++;
    }
    for (int i=0;i < SIZE/2 ; i++)
    {
        int temp = arr[i];
        arr[i] = arr[SIZE - i -1];
        arr[SIZE - i - 1] = temp;
    }

    for (int i =0; i<SIZE; i++){
        cout << *(arr + i)<<" ";
    }

    delete[] arr;


    return 0;
}

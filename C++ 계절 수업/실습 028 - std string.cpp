#include <iostream>
#include <string>

using namespace std;

int main(void){
    string W;
    int arr[26];
    cin >> W;

    for(int i = 0; i <26;i++)
    {
        arr[i] = -1;
    }
    for(int i =0; i<W.length();i++){
        if(arr[(int)W[i]-97]<0) arr[(int)W[i]-97] = i;
    }
    for(int i = 0; i<26; i++){
        cout << arr[i]+1 <<" ";
    }
    return 0;
}
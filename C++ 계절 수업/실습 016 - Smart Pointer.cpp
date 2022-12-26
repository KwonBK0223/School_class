#include <iostream>
#include <memory>
using namespace std;

void update(int* a, int* b);

int main(){
    int a,b;
    cin >> a >> b;
    unique_ptr<int>pa{new int{a}};
    unique_ptr<int>pb{new int{b}};


    update(&a,&b);
    cout << a << endl;
    cout << b << endl;


}
void update(int* a, int* b){
    int temp = *a;
    *a = *a + *b;
    *b = temp - *b;

}
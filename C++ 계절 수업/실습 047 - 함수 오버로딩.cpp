#include <iostream>
#include <map>
#include <string>
using namespace std;

void addItem(map<string,int>& inventory, string item, int count){
    inventory[item] += count;
}
void addItem(map<string,int>& inventory, string item, float money){
    inventory[item] += 1;
    inventory["MONEY"] += money;
}

int main(){
    map<string,int> inventory;
    addItem(inventory,"sword",1);
    addItem(inventory,"shield",2);
    addItem(inventory,"shield",5.0F);
    addItem(inventory,"armor",3.0F);

    for(const auto&[key,value]: inventory)
        cout<<key<<" "<<value<<endl;
}
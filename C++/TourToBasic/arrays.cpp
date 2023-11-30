#include<iostream>

int main(){

    int arrayspertama[] = {1,2,3,4,5};

    for (int i = 0; i < sizeof(arrayspertama)/sizeof(int); i++){

        std::cout << arrayspertama[i] << "\n";

    }

    std::cout << "\n";

    std::string arraykedua[] = {"Wandi","Andi","Ciwan","Wanda","Iwang"};
    for (std::string item : arraykedua){
        std::cout << item << "\n";
    }
    return 0;
}
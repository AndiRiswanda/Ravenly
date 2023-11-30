#include <iostream>

int main() {

    // pointers = variable that stores a memory address of another variable
    //                    sometimes it's easier to work with an address         

    // & address-of operator
    // * dereference operator


    //VARIALE
    std::string name = "Bro";
    int age = 21;
    std::string freePizzas[5] = {"pizza1", "pizza2", "pizza3", "pizza4", "pizza5"};
    
    //THEIR POINTER
    std::string *pName = &name;
    int *pAge = &age;
    std::string *pFreePizzas = freePizzas;
    
    std::cout << "the address of variable store in pointer : \n";
    std::cout << "variable age : " <<*pAge << "\n\twith address" << pAge <<"\n";
    std::cout << "variable name : " <<*pName << "\n\twith address" << pName <<"\n";
    
    for (int i = 0 ; i < sizeof(freePizzas) / sizeof(freePizzas[0]); i++){
        std::cout << "The Address of Variable Pizza " << i << ": " << *(pFreePizzas+i) << "\n";


    }

    return 0;
}
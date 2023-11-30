#include<iostream>


int main () { 

    std::string nama;
    std::getline(std::cin, nama);

    if (nama.length() > 12){
        std::cout << ("nama tidak boleh lebih panjang dari 12 kata");
    }
    else{
        std::cout << ("Good\n");
    }
    std::cout << nama.length() << "\n";
    std::cout << nama.append("Helle") << "\n";
    std::cout << nama.empty() << "\n";




    return 0;
}
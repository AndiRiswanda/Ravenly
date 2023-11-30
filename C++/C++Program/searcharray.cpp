#include <iostream>

std::string carinama(std::string arraynama[],std::string carian, int size);

int main() {

    std::string carian;
    std::string namaPemain[] = {"Andi", "Ciwan","Wandi", "Wanda"};
    int size = sizeof(namaPemain)/sizeof(std::string);

    std::cout << "Masukan Nama Yang Anda Cari\n : ";
    std::cin >> carian;
    std::cout << carinama(namaPemain,carian,size);


    return 0;
}

std::string carinama(std::string arraynama[], std::string carian, int size){

    for(int i = 0 ; i < size ; i ++ ){
        if (arraynama[i] == carian){
            return arraynama[i];
        }
    
    }
    return "nama tidak ada dalam pencarian";



}

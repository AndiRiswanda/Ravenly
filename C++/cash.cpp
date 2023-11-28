#include <iostream>


int main () {


    int hargabarang;
    int tunai;

    std::cout << "Masukan Harga Barang : " ; std::cin >> hargabarang;
    std::cout << "Masukan Tunai Pembeli : " ; std::cin >> tunai;
    int baki = tunai - hargabarang;

    int c100 = 0;
    int c50 = 0;
    int c25 = 0;
    int c10 = 0;
    int c5 = 0;
    int c1 = 0;
    if (baki == 0 || baki < 0) {

        std::cout << "Tidak ada baki\n";
        std::exit;

    }

    while (baki > 0)
    {
        if (baki >= 100) {

            c100 ++;
            baki -= 100;
        }
        else if (baki >= 50) {

            c50 ++;
            baki -= 50;
        }
        else if (baki >= 25) {

            c25 ++;
            baki -= 25;
        }
        else if (baki >= 10) {

            c10 ++;
            baki -= 10;
        }
        else if (baki >= 5) {

            c5 ++;
            baki -= 5;
        }
        else if (baki >= 1) {

            c1 ++;
            baki -= 1;
        }
        
    }

    
    std::cout << "Kembalian Adalah : \n";
    std::cout << "Sebanyak " << c100 << " Uang 100 Digunakan\n";
    std::cout << "Sebanyak " << c50 << " Uang 50 Digunakan\n";
    std::cout << "Sebanyak " << c25 << " Uang 25 Digunakan\n";
    std::cout << "Sebanyak " << c10 << " Uang 10 Digunakan\n";
    std::cout << "Sebanyak " << c5 << " Uang 5 Digunakan\n";
    std::cout << "Sebanyak " << c1 << " Uang 1 Digunakan\n";


    return 0;
}
#include <iostream>


int main () {


    int hargabarang;
    int tunai;

    std::cout << "Masukan Harga Barang : " ; std::cin >> hargabarang;
    std::cout << "Masukan Tunai Pembeli : " ; std::cin >> tunai;
    int baki = tunai - hargabarang;

    int arraymoney[] = {0,0,0,0,0,0};
    int arraytotalmoney[] = {100,50,25,10,5,1};
    if (baki == 0 || baki < 0) {

        std::cout << "Tidak ada baki\n";
        std::exit;

    }

    for ( int i = 0; i < sizeof(arraymoney)/sizeof(int) ; i++){

        while(baki >= arraytotalmoney[i]){
            arraymoney[i]++;
            baki -= arraytotalmoney[i];
        }


    }
    
    std::cout << "Kembalian Adalah : \n";
    std::cout << "Sebanyak " << arraymoney[0] << " Uang 100 Digunakan\n";
    std::cout << "Sebanyak " << arraymoney[1] << " Uang 50 Digunakan\n";
    std::cout << "Sebanyak " << arraymoney[2] << " Uang 25 Digunakan\n";
    std::cout << "Sebanyak " << arraymoney[3] << " Uang 10 Digunakan\n";
    std::cout << "Sebanyak " << arraymoney[4] << " Uang 5 Digunakan\n";
    std::cout << "Sebanyak " << arraymoney[5] << " Uang 1 Digunakan\n";


    return 0;
}
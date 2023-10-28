#include <iostream>

int main()
{
    //string variable
    std::string sebuahkata = "Hello World!";
    std::cout << sebuahkata << std::endl ;

    //char or chracter variable( hanya bisa menyimpan satu huruf)
    char nilai_huruf = 'A';
    char satu_huruf = 'B';

    std::cout << nilai_huruf << "\n" << satu_huruf << std::endl;

    //Integer Variable(hanya bisa menyimpan nomor bulat / whole number)
    int Umur = 19;
    int jumlahobjek = 20;

    std::cout << Umur << "\n" << jumlahobjek << std::endl;

    //Double variable atau disebut floating point variable ( hanya bisa menyimpan angka dengan decimal)
    //const adalah variable yang dinyatakan read only atau tidak bisa berubah
    const double PI = 3.1415926535;
    double suhu = 20.30;

    std::cout << PI << "\n" << suhu << std::endl;

    //bool atau boolean adalah variable yung menyinpan logic true or false 
    bool lampuhidup = true;
    bool lampumati = false;
    //return disini jika true(1) dan jika false(0)
    std::cout << lampuhidup << "\n" << lampumati << std::endl;


    return 0;


}

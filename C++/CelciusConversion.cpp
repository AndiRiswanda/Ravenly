#include <iostream>

int main() {

    double temp; double celcius; 
    std::cout << "Masukan Suhu dalam Celcius : ";
    std::cin >> celcius;

    if (celcius < 20){

        std::cout << "cuaca hari ini sangat dingin\n";

    }
    else if(celcius >= 20){

        std::cout << "cuaca hari in bagus!\n";


    }
    else{

        std::cout << "cuaca hari ini abnormal";

    }

    std::cout << "\nDalam kelvin suhu saat ini adalah  : "; std::cout<< celcius + 273.15 << "\n";
    std::cout << "\nDalam Reamur suhu saat ini adalah  : "; std::cout<< celcius * 0.8 << "\n";
    std::cout << "\nDalam Fahrenheit suhu saat ini adalah  : "; std::cout<< (celcius * (9/5)) + 32 << "\n";

    return 0;

}
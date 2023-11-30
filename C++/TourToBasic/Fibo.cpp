#include <iostream>



int main () {

    int a = 0; int b = 1; int c = 0;
    int n;
    std::cout << "Urutan Fibonaci ke : ";
    std::cin >> n;
    
    for (int i = 0 ; i < n ; i++){

        std::cout << a << " ";
        c = b;
        b = a + b;
        a = c;
    }


    return 0 ;
}

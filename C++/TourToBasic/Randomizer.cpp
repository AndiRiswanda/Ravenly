#include <iostream>


int main() {

    srand(time(0));

    for (int i = 0; i < 5; i++){
        int nomor = rand() % 5 + 1 ;
        printf("%d",nomor);
    }


    return 0;
}
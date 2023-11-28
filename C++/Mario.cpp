#include <iostream>

int main () {
    
    int n = 50; 

    for (int i = 1; i <= n ; i++){
        
        for(int j = 0; j <= n-i ; j++){

            std::cout <<  " ";
        }
        for(int k = 0; k < i ; k++){

            std::cout <<  "#";
        }
        
    
        for(int l = 1; l < i ; l++){

            std::cout <<  "#";
        }
        
        std::cout << "\n";

    }


    return 0;
}
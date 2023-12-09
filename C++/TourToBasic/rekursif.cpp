#include <iostream>

int faktorial(const int number);

int main () {

    std::cout << faktorial(3);


    return 0;
}

int faktorial(const int number){
    
    if(number < 2){

        return number;
    }
    else{return number * faktorial(number - 1);}
    

}


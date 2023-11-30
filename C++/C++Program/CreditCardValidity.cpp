#include <iostream>

int getnumber (const std::string number);
int sumodd (const std::string number);
bool validcreditcard (const int creditcardnumber);


int main(){

    std::string creditcard = "6011000990139424";

    std::cout << validcreditcard(getnumber(creditcard) + sumodd(creditcard));

    return 0 ;
}

int ntos(int value){
    return value % 10 + (value / 10 % 10);
}

int getnumber (const std::string number){

    int out = 0;
    for (int i = number.length() - 2 ; i >= 0 ; i -= 2){
        out += ntos((number[i] - '0' )*2) ;
    }
    return out;
}

int sumodd (const std::string number){
    int out = 0;
    for (int i = number.length() - 1; i >= 0 ; i-=2){
            out += (number[i] - '0');
        }
    return out;
}

bool validcreditcard (const int creditcardnumber){
    if (creditcardnumber % 10 == 0){
        return true;
    }
    else{return false;}
}
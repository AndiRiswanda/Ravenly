#include <iostream>
//typedef mmebenarkan kita memberikan alias data types, user define data types dan pointer ke alias lain
typedef std::string str;
typedef int integer;


int main() {
    using std::cout;

    str kata = "Hello World\n";
    cout << kata;

    integer nomor = 100;
    cout << nomor;

    


}
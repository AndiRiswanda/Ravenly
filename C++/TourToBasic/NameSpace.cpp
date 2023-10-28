#include <iostream>

//namespace
namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}

int main() {
    using std::cout;
    using std::endl;

    
    cout << first::x << endl;
    cout << second::x << endl; 


}
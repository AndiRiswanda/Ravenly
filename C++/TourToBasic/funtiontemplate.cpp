#include <iostream>
//overloaded fuuntion
int max(int x,int y){
    return (x > y) ? x : y;
}
float max(float x,float y){
    return (x > y) ? x : y;
}

//more effective approch

template <typename T, typename U>

auto min(T x,U y){
    return (x < y) ? x : y;
}


int main (){

    using std::cout;

    cout << max(2,3) << std::endl;

    cout << min(2,3) << std::endl;

    cout << min(2,3.3) << std::endl;
    

    return 0;
}



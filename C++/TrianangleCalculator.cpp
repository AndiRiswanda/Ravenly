#include<iostream>
#include<cmath>

using std::cout;
float triangleC(double a,double b) {

    double z = sqrt(pow(a,2) + pow(b,2));
    
    return z;

}

int main() {
    
    cout << "nilai c =  " << triangleC(4,5) << std::endl;

}
#include<iostream>

int main(){
    
    double nilaisiswa ;

    std::cout << "Masukan Nilai Siswa : " ; std::cin >> nilaisiswa;

    if (nilaisiswa >= 85 && nilaisiswa <=100){
        std::cout << "Grade : A";
    }
    else if (nilaisiswa >= 75 && nilaisiswa <= 84)
    {
        std::cout << "Grade : B";
    }
    else if (nilaisiswa >= 60 && nilaisiswa <= 74)
    {
        std::cout << "Grade : C";
    }
    else if (nilaisiswa >= 30 && nilaisiswa <= 59)
    {
        std::cout << "Grade : D";
    }
    else if (nilaisiswa >= 10 && nilaisiswa <= 29)
    {
        std::cout << "Grade : E";
    }    
    else if (nilaisiswa >= 0 && nilaisiswa <= 28)
    {
        std::cout << "Grade : F";
    }
    
   return 0; 
    




}
#include<iostream>

int main(){
    using std::cout;
    using std::cin;

    std::string nama;
    int umur;
    
    cout << "Apa Nama Kamu?     :   "; std::getline(cin >> std::ws,nama);
    cout << "Berapa Umur Kamu?  :   "; cin >> std::ws >> umur;
    cout << "Nama kamu adalah " << nama << std::endl;
    cout << "kamu berusia " << umur << " tahun";


}
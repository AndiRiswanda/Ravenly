#include<iostream>

int main () {

    //membuat list menu
    std::string menumakanan[]  = {"Pizza","Nasi Kuning","Nasi Lemak","Ayam Goreng"};
    std::string order[5];
    
    std::cout << "--------------------------\n";
    std::cout << "      Selamat Datang      \n";
    std::cout << "--------------------------\n";
    std::cout << "Silahkan Pilih Menu Dibawah\n";
    for (int i  = 0 ; i < sizeof(menumakanan)/sizeof(std::string) ; i++){
        
        std::cout << i+1 << ". "<< menumakanan[i] << "\n";
        }
    int choice;
    for (int i  = 0; i < 4 ; i++){
    std::cin >> choice;
    switch (choice){
        case 1 :
            order[i] = "pizza";
            break;
        case 2 :
            order[i] = "Nasi Kuning";
            break;
        case 3 :
            order[i] = "Nasi Lemak";
            break;
        case 4 :
            order[i] = "Ayam Goreng";
            break;
    }
    system("cls");
    std::cout << "--------------------------\n";
    std::cout << "      Selamat Datang      \n";
    std::cout << "--------------------------\n";
    std::cout << "Silahkan Pilih Menu Dibawah\n";
    for (int i  = 0 ; i < sizeof(menumakanan)/sizeof(std::string) ; i++){
        
        std::cout << i+1 << ". "<< menumakanan[i] << "\n";
        }
    }
    system("cls");
    std::cout << "--------------------------\n";
    std::cout << "   Pesanan Kamu adalah     \n";
    std::cout << "--------------------------\n";
    for (int i  = 0 ; !order[i].empty() ; i++){
        
    std::cout << i+1 << ". "<< order[i] << "\n";
    }



    return 0;
}
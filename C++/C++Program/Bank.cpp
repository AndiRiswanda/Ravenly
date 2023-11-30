#include<iostream>
#include<cstdlib>
void cekbalance(double balance);
double withdrawmoney();
double insertmoney();
int main() {  

    double balance = 0;
    double depo;
    int choice;
    std::cout << "|------------------------|\n";
    std::cout << "|       Bank Ciwan       |\n";
    std::cout << "|------------------------|\n";
    std::cout << "|-------Pilih Opsi-------|\n";
    std::cout << "|------------------------|\n";
    std::cout << "    1. Check Balance\n";
    std::cout << "    2. Withdraw Money\n";
    std::cout << "    3. Insert Money\n";
    std::cout << "    4. exit\n";
    std::cout << "    Input Pilihan Anda\n   : ";
    
    do{
        scanf("%d",&choice);
        system("cls");
        switch (choice)
        {
        case 1:
            cekbalance(balance);
            break;
        case 2:
            balance += withdrawmoney();
            break;
        case 3:
            balance += insertmoney();
            break;
        default:
            break;
        }

        std::cout << "|------------------------|\n";
        std::cout << "|-------Pilih Opsi-------|\n";
        std::cout << "|------------------------|\n";
        std::cout << "    1. Check Balance\n";
        std::cout << "    2. Withdraw Money\n";
        std::cout << "    3. Insert Money\n";
        std::cout << "    4. exit\n";
        std::cout << "    Input Pilihan Anda\n   : ";
    }while(choice != 4);

return 0;
}


void cekbalance (double balance){
    printf("Balance Anda Saat Ini Adalah\n : %.0lf \n", balance);
}
double withdrawmoney(){
    double depo = 0;
    std::cout << "Jumlah tarikan : \n";
    scanf("%lf", &depo);
    depo = -depo;
    return depo;
}
double insertmoney(){
    double depo = 0;
    std::cout << "Jumlah Masukan : \n";
    scanf("%lf", &depo);
    depo = depo;
    return depo;
}

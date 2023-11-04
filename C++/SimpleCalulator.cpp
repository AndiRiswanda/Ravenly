#include<iostream>

int main() {

    char operan;
    double num1;
    double num2;
    std::cout << "######## Calulator ########\n\n";
    std::cout << "Choose Operant ( + - * / ): "; std::cin >> operan;
    std::cout << "Enter the first number : \n"; std::cin >> num1;
    std::cout << "Enter the second number : \n"; std::cin >> num2;

    switch (operan)
    {
    case '+':
        std::cout << "Result = " << num1 + num2 << std::endl;
        break;
    case '-':
        std::cout << "Result = " << num1 - num2<< std::endl;
        break;
    case '/':
        std::cout << "Result = " << num1 / num2<< std::endl;
        break;
    case '*':
        std::cout << "Result = " << num1 * num2<< std::endl;
        break;
    
    default:std::cout << "Operan Invalid";
        break;
    }
    return 0;
    
    std::cout << "\n\n###########################";
}
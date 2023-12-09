#include <iostream>

class students{
    public:
        std::string name;
        int age;
        float gpa;

    //intializer
    students(std::string name,int age, double gpa){
        this-> name = name;
        this-> age = age;
        this-> gpa = gpa;
    }

    //method
    void showattribute(){
        std::cout << "Name : " << this->name << std::endl;
        std::cout << "Age : " << this->age << std::endl;
        std::cout << "GPA : " << this->gpa << "\n";
    }

};

int main () {
    students wandi("Andi Riswanda",18,3.9);
    students ivan("Ivan Betrandi",20,3.5);
    wandi.showattribute();
    ivan.showattribute();





    return 0;
}
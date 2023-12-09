#include <iostream>

class employe{

    private:
        int salary;
    public:
        std::string Name;
        float workEffcienty;

    //initialization
    employe(int salary,std::string Name, float workEffcienty) : salary(salary), Name(Name), workEffcienty(workEffcienty){}
    
    void setSalary(int newsalary){
        this->salary = newsalary;
    }
    void printAttributes(){
        std::cout << "Name : " << Name << "\n";
        std::cout << "Salary : RM." << salary << "\n";
        std::cout << "Work Efficien : " << workEffcienty << "\n";
    }

};



int main (){

    employe riswanda(200000,"Andi Riswanda", 10.5);
    riswanda.printAttributes();


    return 0;
}
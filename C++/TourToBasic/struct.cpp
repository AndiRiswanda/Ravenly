#include <iostream>

/*
almost the same as class in python 
*/





struct students
{
    std::string name;
    float gpa ;
    bool endroled;
};

void studentsnamechance(students &students, std::string newname){
    students.name = newname;
}



int main (){


    students students1;
    students1.name = "ciwang";
    students1.gpa = 4.0;
    students1.endroled = true;

    std::cout << students1.name << "\n";
    studentsnamechance(students1, "Wandi");
    std::cout << students1.name << "\n";

    return 0;
}
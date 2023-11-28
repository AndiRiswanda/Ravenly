#include <iostream>
#include <cstdio>

int main() {
    int integer1;
    long integer2;
    char c;
    float f;
    double d;
    
    scanf("%d %ld %c %f %lf", &integer1,&integer2,&c,&f,&d);
    
    printf("%d\n%ld\n%c\n%.3f\n%.9lf",integer1,integer2,c,f,d);
    
    return 0;
}
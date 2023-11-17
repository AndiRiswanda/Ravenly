#include <iostream>

bool isPrime(long long z) {
    if (z <= 2) {
        return false;
    } else {
        for (long long i = 2; i < z; i++) {
            if (z % i == 0) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    std::cout << std::boolalpha << isPrime(9223372036854775807) << std::endl;
    return 0;
}

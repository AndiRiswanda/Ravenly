#include <iostream>




int main(){

    int unsorted[] = {3, 4, 7, 8, 5,  6, 1, 2};
    int length = sizeof(unsorted)/sizeof(int);
    for (int i = 0; i < length - 1; i++){
        for (int j = 0; j < length - i - 1 ; j++){
            if (unsorted[j+1] < unsorted[j]){
                int temp = unsorted[j];
                unsorted[j] = unsorted[j+1];
                unsorted[j+1] = temp;
            }
        }
    }
    for (int item : unsorted){
        if (item != unsorted[0]){std::cout << " " << item;}
        else if (item == unsorted[0]){std::cout << item;}
    }


    return 0;
}
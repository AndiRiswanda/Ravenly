#include <iostream>

bool sortedarray(int array[], int length);


int main(){

    int unsorted[] = {1 , 2  , 3 , 4 , 5 , 7 , 9 , 6 , 8 , 10};
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


#include <stdio.h>

int main() {
    // Initialize the arrays
    int array1[] = {20, 10, 11, 7, 4};
    int array2[] = {60, 50, 30, 27, 17};
    int size1 = 5; // Size of array1
    int size2 = 5; // Size of array2
    int mergedArray[10]; // Array to hold the merged elements
    int i;

    // Merge array1 and array2 into mergedArray
    for (i = 0; i < size1; i++) {
        mergedArray[i] = array1[i];
    }
    for (i = 0; i < size2; i++) {
        mergedArray[size1 + i] = array2[i];
    }

    // Print the unsorted merged array
    printf("Unsorted Merged Array: ");
    for (i = 0; i < size1 + size2; i++) {
        printf("%d ", mergedArray[i]);
    }
    
    return 0;
}


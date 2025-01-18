#include <stdio.h>

// Function to find the largest element in the array recursively
int findLargest(int arr[], int index, int size) {
    // Base case: when the last element is reached
    if (index == size - 1)
        return arr[index];
    
    // Recursive call to find the largest in the rest of the array
    int largest = findLargest(arr, index + 1, size);
    
    // Return the larger between the current element and the largest found in the rest
    return (arr[index] > largest) ? arr[index] : largest;
}

int main() {
    int arr[] = {12, 34, 54, 2, 93, 18};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    int largest = findLargest(arr, 0, size);
    
    printf("The largest element is: %d\n", largest);
    return 0;
}


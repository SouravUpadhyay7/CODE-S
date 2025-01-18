#include <stdio.h>

// Function for binary search
int binarySearch(int arr[], int n, int key) {
    int left = 0, right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Check if key is present at mid
        if (arr[mid] == key)
            return mid;

        // If key is greater, ignore the left half
        if (arr[mid] < key)
            left = mid + 1;

        // If key is smaller, ignore the right half
        else
            right = mid - 1;
    }

    // Key was not present in the array
    return -1;
}

int main() {
    int n, key;
    
    // Take user input for the number of elements
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    
    // Take user input for the elements of the array
    printf("Enter the elements (sorted in ascending order): ");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    // Take user input for the key to be searched
    printf("Enter the key to search: ");
    scanf("%d", &key);
    
    // Perform binary search
    int result = binarySearch(arr, n, key);
    
    // Print the result
    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");
    
    return 0;
}


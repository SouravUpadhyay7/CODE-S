#include <stdio.h>

void linearSearch(int arr[], int n, int key) {
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            printf("Key found at index %d\n", i);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("Key not found\n");
    }
}

int main() {
    int n, key;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    printf("Enter the elements: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    printf("Enter the key to search: ");
    scanf("%d", &key);
    
    linearSearch(arr, n, key);
    
    return 0;
}


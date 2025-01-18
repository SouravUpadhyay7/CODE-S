#include <stdio.h>

// Function to check if a number is prime using recursion
int isPrime(int num, int divisor) {
    // Base case: If divisor reaches 1, the number is prime
    if (divisor == 1)
        return 1;  // Prime
    
    // If num is divisible by divisor, it's composite
    if (num % divisor == 0)
        return 0;  // Not prime
    
    // Recursive case: check with the next divisor
    return isPrime(num, divisor - 1);
}

int main() {
    int num;

    // Input number from user
    printf("Enter a number: ");
    scanf("%d", &num);

    // Handling edge cases for numbers less than or equal to 1
    if (num <= 1) {
        printf("%d is neither prime nor composite.\n", num);
    } else {
        // Call isPrime function starting from num-1 as divisor
        if (isPrime(num, num - 1))
            printf("%d is a prime number.\n", num);
        else
            printf("%d is a composite number.\n", num);
    }

    return 0;
}


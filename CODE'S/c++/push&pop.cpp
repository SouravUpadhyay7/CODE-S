#include <stdio.h>
#define MAX 5  // Maximum size of the stack

int stack[MAX];
int top = -1;  // Indicates an empty stack

// Function to push an element onto the stack
void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow! Cannot push %d\n", value);
    } else {
        top++;
        stack[top] = value;
        printf("%d pushed onto the stack.\n", value);
    }
}

// Function to pop an element from the stack
void pop() {
    if (top == -1) {
        printf("Stack Underflow! No elements to pop.\n");
    } else {
        printf("%d popped from the stack.\n", stack[top]);
        top--;
    }
}

int main() {
    // Performing push operations
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);
    push(60);  // Stack overflow will occur here

    // Performing pop operations
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();  // Stack underflow will occur here

    return 0;
}


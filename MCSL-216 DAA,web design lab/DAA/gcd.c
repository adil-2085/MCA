#include <stdio.h>

void hornersMethod(int coeffs[], int size, int x) {
    int result = coeffs[0];
    int mult_count = 0;
    int add_count = 0;
    int loop_iterations = 0;

    for (int i = 1; i < size; i++) {
        loop_iterations++;
        result = (result * x) + coeffs[i];
        mult_count++;
        add_count++;
    }

    printf("--- Horner's Method (Q2 Part i) ---\n");
    printf("Result: %d\n", result);
    printf("Multiplications: %d\n", mult_count);
    printf("Additions: %d\n", add_count);
    printf("Loop Iterations: %d\n\n", loop_iterations);
}

void bruteForceMethod(int coeffs[], int size, int x) {
    int n = size - 1;
    int total_val = 0;
    int mult_count = 0;
    int add_count = 0;

    for (int i = 0; i < size; i++) {
        int degree = n - i;
        int term_val = coeffs[i];

        if (degree > 0) {
            int x_power = 1;
            for (int j = 0; j < degree; j++) {
                x_power *= x;
                mult_count++;
            }
            term_val = coeffs[i] * x_power;
            mult_count++;
            add_count++;
        }
        total_val += term_val;
    }

    printf("--- Brute Force Method (Q2 Part ii) ---\n");
    printf("Result: %d\n", result); // Note: total_val
    printf("Multiplications: %d\n", mult_count);
    printf("Additions: %d\n", add_count);
}

int main() {
    // Coefficients for 6x^6 + 5x^5 + 4x^4 - 3x^3 + 2x^2 + 8x - 7
    int coefficients[] = {6, 5, 4, -3, 2, 8, -7};
    int size = sizeof(coefficients) / sizeof(coefficients[0]);
    int x_val = 3;

    hornersMethod(coefficients, size, x_val);
    bruteForceMethod(coefficients, size, x_val);

    return 0;
} 
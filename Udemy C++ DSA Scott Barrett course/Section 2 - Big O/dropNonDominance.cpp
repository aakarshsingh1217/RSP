#include <iostream>

void printItems(int n) {
    // these nested for loops still run O(n^2) times
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cout << i << j << std::endl;
        }
    }

    // single for loop ran n time, so total num of operations was O(n^2) +
    // O(n) or O(n^2 + n), n^2 dominant term and n non dominant, when n becomes
    // 100 n^2 is 10000, standalone n as the number gets larger and larger becomes
    // less and less significant in equation. So simplify by dropping n and leaving
    // O(n^2), rule of simplification called drop non dominants
    for (int k = 0; k < n; k++) {
        std::cout << k << std::endl;
    }
}

int main() {
    printItems(10);

    return 0;
}
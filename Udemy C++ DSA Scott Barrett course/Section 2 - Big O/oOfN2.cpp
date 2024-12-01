#include <iostream>

void printItems(int n) {
    // inner for loop will have different outcome. this will run n*n
    // times = n^2, which is O(n^2). On a graph,  O(n^2) grows much
    // faster than O(n) (much less efficient than O of n). So, O(n)
    // better way to write functions, and  O(n^2) least efficient big O.
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cout << i << j << std::endl;
        }
    }
}

int main() {
    printItems(10);

    return 0;
}
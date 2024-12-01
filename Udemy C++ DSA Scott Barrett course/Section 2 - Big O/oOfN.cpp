#include <iostream>

void printItems(int n) {
    // O(n), because it will run n times. X axis is n, Y axis is num of
    // operations, O(n) is a straight line and is called 'proportial'
    for (int i = 0; i < n; i++) {
        std::cout << i << std::endl;
    }

    // this plus other function run n + n times, drop constant so it's
    // O(n), doesn't matter if it's 2n or 100n, drop constant because
    // we care about the broad category that the growth rate is in.
    // at 100n, it's growing linerally as oppossed to exponentially,
    // which is in a different category
    for (int j = 0; j < n; j++) {
        std::cout << j << std::endl;
    }
}

int main() {
    printItems(10);

    return 0;
}
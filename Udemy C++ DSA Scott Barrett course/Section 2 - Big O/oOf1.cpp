#include <iostream>

// first big O where number of operations does not change as n becomes larger.
// if n is one, one operation occurs (addition). if n went to 1 million, still 1
// operation, addition. Therefore, it's O(1).
int addItems(int n) {
    return n + n;
}

// even if its n + n + n, two operations becomes O(2), but we simplify it and call it
// O(1). O(1) runs linerarly across the bottom of the graph (x axis) and is the most
// efficient big O, because as N becomes larger the number of operations does not
// become larger. O(1) time complexity functions are very efficient.
int addItems2(int n) {
    return n + n + n;
}
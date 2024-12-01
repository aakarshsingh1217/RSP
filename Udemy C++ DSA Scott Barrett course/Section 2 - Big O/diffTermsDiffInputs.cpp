#include <iostream>

// people make the mistake that first and second for loops are o(n) which becomes
// o(2n) and dropped constant = o(n), but you can't do that. if you think of it as
// a algebra prob., you cant say a=n and b=n, theyre different terms. need to say
// first for loop is o(a) and 2nd is o(b) and added together is o(a + b) and that's
// as far as you can simplify this
void printItems(int a, int b) {
    for (int i = 0; i < a; i++) {
        std::cout << i << std::endl;
    }

    for (int j = 0; j < b; j++) {
        std::cout << j << std::endl;
    }
}

// likewise, if you have a for loop inside of a for loop, you would say that this o(a * b)
// , you have to show these vars seperately. you have to show different terms for inputs.
void printItems(int a, int b) {
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            std::cout << i << j << std::endl;
        }
    }
}
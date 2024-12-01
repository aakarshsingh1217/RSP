#include <iostream>

int main() {
    /*
    // when we set num 2 to be equal to num 1, we're passing the value down to num2 (not
    // using a pointer)
    int num1 = 11;
    int num2 = num1;

    // num1 becomes 22 and num2 stays 11 (this is how it works when you're not using
    // a pointer)
    num1 = 22;

    std::cout << "num1 = " << num1 << std::endl;
    std::cout << "num2 = " << num2 << std::endl;
    */

   // * means num1 is now a pointer, when we set this to be equal to 11 we use new int(11),
   // which creates a new integer somewhere in memory that has a value of 11 and we're
   // num1 to that integer we've created.
   int* num1 = new int(11);
   // then we say num2 is equal to num1 but with the *, which makes num2 a pointer as well.
   // num1 points to new int(11) in memory and when we set num two to be equal to num one,
   // what we're doing is passing the reference (the pointer) and num2 points to the same
   // integer in memory that num one is pointing to.
   int* num2 = num1;

    // setting int that num1 points to, to 22, now both nums will be 22.
   *num1 = 22;

    // num1 and num2 are equal to an address in memory, to print out numbers add stars
    // to vars so that it prints out integer at the address in memory the pointers are
    // pointing to
    std::cout << "num1 = " << *num1 << std::endl;
    std::cout << "num2 = " << *num2 << std::endl;

    // pointers important because when you use DS like linked list, we can say number 22
    // could be a node, the first node in the linked list is going to have a pointer to
    // it aclled head, head is a variable that is a pointer to a node. if we create
    // another variable called temp, and we set it equal to head, what we're doing is
    // having it point to the exact same node that head is pointing to. 22 is also
    // a pointer that can point to another node (e.g. num 44), if we set head to be
    // equal to number 44 pointer, next head would be 44.
    // we can take pointers that're pointing to some object in memory and point them
    // at another object in memory (pointers aren't permanent). if you create another
    // pointer to an integer (num3 = 44), and if we set num2 to be equal to num3 it
    // will start pointing at num3 (44), pointers can be redirected.

    return 0;
}
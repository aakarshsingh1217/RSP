#include <iostream>

using namespace std;

class Node {
    public:
        Node* next;
        int value;

        Node(int value) {
            this->value = value;
            next = nullptr;
        }
};

class Stack {
    private:
        Node* top;
        int height;

    public:
        Stack(int value) {
            Node* newNode = new Node(value);
            top = newNode;
            height = 1;
        }

        int pop() {
            if(height == 0) return INT_MIN;

            Node* temp = top;
            int poppedValue = top->value;
            top = top->next;
            delete temp;
            height--;

            return poppedValue;
        }
};

int main() {
    Stack* myStack = new Stack(1);
    cout << "Popped value: " << myStack->pop();
    cout << "\n\nPopped value: " << myStack->pop();
    
    return 0;
}
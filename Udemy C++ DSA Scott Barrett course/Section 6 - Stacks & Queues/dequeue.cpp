#include <iostream>

class Node {
    public:
        Node* next;
        int value;

        Node(int value) {
            this->value = value;
            next = nullptr;
        }
};

class Queue {
    private:
        Node* first;
        Node* last;
        int length;

    public:
        Queue(int value) {
            Node* newNode = new Node(value);
            first = newNode;
            last = newNode;
            length = 1;
        }

        int dequeue() {
            if(length == 0) return INT_MIN;
            Node* temp = first;
            int dequeuedValue = first->value;
            if(length == 1) {
                first = nullptr;
                last = nullptr;
            } else {
                first = first->next;
            }
            delete temp;
            length--;
            return dequeuedValue;
        }
};
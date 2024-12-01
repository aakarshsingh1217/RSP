#include <iostream>

using namespace std;

class Node {
    public:
        int value;
        Node* next;
        Node* prev;

        Node(int value) {
            this->value = value;
            next = nullptr;
            prev = nullptr;
        }
};

class DoublyLinkedList {
    private:
        Node* head;
        Node* tail;
        int length;

    public:
        DoublyLinkedList(int value) {
            Node* node = new Node(value);
            head = node;
            tail = node;
            length = 1;
        }

        Node* get(int index) {
            if(index < 0 || index >= length) {
                return nullptr;
            }
            Node* temp = head;
            if(index < length/2) {
                for(int i = 0; i < index; i++) {
                    temp = temp->next;
                }
            } else {
                temp = tail;
                for(int i = length - 1; i > index; i--) {
                    temp = temp->prev;
                }
            }
            return temp;
        }

        void printList() {
            Node* temp = head;
            while(temp != nullptr) {
                cout << temp->value << endl;
                temp = temp->next;
            }
        }

        void append(int value) {
            Node* newNode = new Node(value);
            if(length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                newNode->prev = tail;
                tail = newNode;
            }

            length++;
        }

        bool set(int index, int value) {
            Node* temp = get(index);
            if(temp) {
                temp->value = value;
                return true;
            }
            return false;
        }
};

int main() {
    DoublyLinkedList* myDLL = new DoublyLinkedList(11);
    myDLL->append(3);
    myDLL->append(23);
    myDLL->append(7);

    myDLL->set(1, 4);

    myDLL->printList();
}
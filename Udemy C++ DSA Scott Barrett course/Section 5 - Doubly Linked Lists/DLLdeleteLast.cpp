#include <iostream>

using namespace std;

class Node {
    public:
        int value;
        Node* prev;
        Node* next;

        Node(int value) {
            this->value = value;
            prev = nullptr;
            next = nullptr;
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

        void deleteLast() {
            if(length == 0) return;
            Node* temp = tail;
            if(length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                tail = tail->prev;
                tail->next = nullptr;
            }
            delete temp;
            length--;
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
            delete newNode;
            length++;
        }

        void printList() {
            Node* temp = head;
            while(temp != nullptr) {
                cout << temp->value << endl;
                temp = temp->next;
            }
        }
};

int main() {
    DoublyLinkedList* myDLL = new DoublyLinkedList(1);
    myDLL->append(2);

    cout << "DLL before deleteLast():\n";
    myDLL->printList();

    myDLL->deleteLast();
    cout << "\n\nDLL after 1st deleteLast():\n";
    myDLL->printList();

    myDLL->deleteLast();
    cout << "\n\nDLL after 2nd deleteLast():\n";
    myDLL->printList();

        myDLL->deleteLast();
    cout << "\n\nDLL after 3rd deleteLast():\n";
    myDLL->printList();

    return 0;
}
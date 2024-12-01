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

        void printList() {
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->value << endl;
                temp = temp->next;
            }
        }

        void deleteFirst() {
            if(length == 0) return;
            Node* temp = head;
            if(length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->next;
                head->prev = nullptr;
            }
            delete temp;
            length--;
        }
};

int main() {
    DoublyLinkedList* myDLL = new DoublyLinkedList(2);
    myDLL->append(1);

    cout << "DLL before deleteFirst():\n";
    myDLL->printList();

    myDLL->deleteFirst();
    cout << "\n\nDLL after 1st deleteFirst():\n";
    myDLL->printList();
    
    myDLL->deleteFirst();
    cout << "\n\nDLL after 2nd deleteFirst():\n";
    myDLL->printList();

    myDLL->deleteFirst();
    cout << "\n\nDLL after 3rd deleteFirst():\n";
    myDLL->printList();
}
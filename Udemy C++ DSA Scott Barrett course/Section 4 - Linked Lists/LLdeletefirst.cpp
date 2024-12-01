#include <iostream>

using namespace std;

class Node {
    public:
        int value;
        Node* next;

        Node(int value) {
            this->value = value;
            next = nullptr;
        }
};

class LinkedList {
    private:
        Node* head;
        Node* tail;
        int length;

    public:
        LinkedList(int value) {
            Node* node = new Node(value);
            head = node;
            tail = node;
            length = 1;
        }

        ~LinkedList() {
            Node* temp = head;
            while(head) {
                head = head->next;
                delete temp;
                temp = head;
            }
        }

        void append(int value) {
            Node* newNode = new Node(value);
            if(length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }

            length++;
        }

        void deleteFirst() {
            if(length == 0) return;
            Node* temp = head;
            if(length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->next;
            }
            delete temp;
            length--;
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
    LinkedList* myLinkedList = new LinkedList(2);
    myLinkedList->append(1);

    cout << "LL before deleteFirst():\n";
    myLinkedList->printList();

    myLinkedList->deleteFirst();
    cout << "\n\nLL after 1st deleteFirst():\n";
    myLinkedList->printList();

    myLinkedList->deleteFirst();
    cout << "\n\nLL after 2nd deleteFirst():\n";
    myLinkedList->printList();

    myLinkedList->deleteFirst();
    cout << "\n\nLL after 3rd deleteFirst():\n";
    myLinkedList->printList();

    return 0;
}
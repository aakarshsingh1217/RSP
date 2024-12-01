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

class LinkedList{
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

        void deleteFirst() {
            if(length == 0) return;
            Node* temp = head;
            if(length ==1) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->next;
            }
            delete temp;
            length--;
        }

        void deleteLast() {
            if(length == 0) return;
            Node* temp = head;
            if(length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                Node* pre = head;
                while(temp->next) {
                    pre = temp;
                    temp = temp->next;
                }
                tail = pre;
                tail->next = nullptr;
            }
            delete temp;
            length--;
        }

        Node* get(int index) {
            if(index < 0 || index >= length) {
                return nullptr;
            }
            Node* temp = head;
            for(int i = 0; i < index; i++) {
                temp = temp->next;
            }
            return temp;
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

        void printList() {
            Node* temp = head;
            while(temp != nullptr) {
                cout << temp->value << endl;
                temp = temp->next;
            }
        }

        void deleteNode(int index) {
            if(index < 0 || index >=length) return;
            if(index == 0) return deleteFirst();
            if(index == length - 1) return deleteLast();

            Node* prev = get(index - 1);
            Node* temp = prev->next;

            prev->next = temp->next;
            delete temp;
            length--;
        }
};

int main() {
    LinkedList* myLinkedList = new LinkedList(1);
    myLinkedList->append(2);
    myLinkedList->append(3);
    myLinkedList->append(4);
    myLinkedList->append(5);

    cout << "LL before deleteNote():\n";
    myLinkedList->printList();

    myLinkedList->deleteNode(2);
    cout << "LL after deleteNote() in middle:\n";
    myLinkedList->printList();

    myLinkedList->deleteNode(0);
    cout << "LL after deleteNote() of first node:\n";
    myLinkedList->printList();

    myLinkedList->deleteNode(2);
    cout << "LL after deleteNote() of last node:\n";
    myLinkedList->printList();
    return 0;
}
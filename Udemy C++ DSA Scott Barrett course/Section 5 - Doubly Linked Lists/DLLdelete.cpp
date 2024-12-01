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
                for(int i = length-1; i > index; i--) {
                    temp = temp->prev;
                }
            }
            return temp;
        }

        void deleteNode(int index) {
            if(index < 0 || index >= length) return;
            if(index == 0) return deleteFirst();
            if(index == length - 1) return deleteLast();
            Node* temp = get(index);
            temp->next->prev = temp->prev;
            temp->prev->next = temp->next;
            delete temp;
            length--;
        }
};
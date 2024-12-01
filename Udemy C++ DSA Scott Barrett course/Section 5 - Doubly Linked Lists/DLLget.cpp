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
};
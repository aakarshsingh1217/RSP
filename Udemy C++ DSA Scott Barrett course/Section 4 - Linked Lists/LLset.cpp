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

        bool set(int index, int value) {
            Node* temp = get(index);
            if(temp) {
                temp->value = value;
                return true;
            }
            return false;
        }
};
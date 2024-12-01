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

        void prepend(int value) {
            Node* newNode = new Node(value);
            if(length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                newNode->next = head;
                head->prev = newNode;
                head = newNode;
            }
            length++;
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

        bool insert(int index, int value) {
            if(index < 0 || index > length) return false;
            if(index == 0) {
                prepend(value);
                return true;
            }
            if(index == length) {
                append(value);
                return true;
            }
            Node* newNode = new Node(value);
            Node* before = get(index - 1);
            Node* after = before->next;
            newNode->prev = before;
            newNode->next = after;
            before->next = newNode;
            after->prev = newNode;
            length++;
            return true;
        }
};
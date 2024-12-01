// seperate class that just creates nodes
// when 3 linkedlist member funcs need to create a node, they call the node class to
// do that

class Node {
    public:
        //node class needs member values of value and next, similar to unordered map
        int value;
        Node* next; // pointer that points to a node

        //constructor we pass value to
        Node(int value) {
            //this->value equal to value is the member var value
            this->value = value;
            // dont need this as we dont have next as param for node func.
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
            //for LL constructor, we're going to create the first node in the linked list 
            //at the time we create the linkedlist

            // this will create our first node, e.g. val passed 4 means
            // node is created newNode->4->nullptr
            Node* newNode = new Node(value);
            // head is a pointer to a node and new node is a pointer to a node
            // when head is equal to new node, you want to be point this var
            // head at the same node that new node is pointing to 
            // head + newNode -> 4 -> nullptr
            head = newNode;
            tail = newNode;
            // now head + tail -> 4 -> nullptr
            length = 1;
            // one node in linkedList so length is 1
        }

    // all three member funcs. get passed a value
    // all three member funcs. create a new node

    //append will create a new node and add that node to the end
    void append(int value) {
        //create new Node
        //add Node to end
    }

    //prepend create new node and add Node to beginning
    void prepend(int value) {
        //create new Node
        //add Node to beginning
    }

    //insert will create a new node and insert that node at a particular index
    bool insert(int index, int value) {
        //create new Node
        //insert Node
    }
};

int main() {
    LinkedList* myLinkedList = new LinkedList(4); //create LL
    // we get head + tail -> 4 -> nullptr, length = 1

    return 0;
}
class Node {
    public:
        int value;
        Node* left;
        Node* right;

        Node(int value) {
            this->value = value;
            left = nullptr;
            right = nullptr;
        }
};

class BinarySearchTree {
    public:
        Node* root;

        BinarySearchTree() {
            root = nullptr;
        }

        bool contains(int value) {
            Node* temp = root;
            while(temp) {
                if(value < temp->value) {
                    temp = temp->left;
                } else if(value > temp->value) {
                    temp = temp->right;
                } else {
                    return true;
                }
            }
            return false;
        }
};

int main() {


    return 0;
}
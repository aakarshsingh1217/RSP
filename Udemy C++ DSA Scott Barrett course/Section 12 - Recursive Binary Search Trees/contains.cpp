#include <iostream>

using namespace std;

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
    private:
        Node* root;

    public:
        BinarySearchTree() {
            root = nullptr;
        }

        bool insert(int value) {
            Node* newNode = new Node(value);
            if(root == nullptr) {
                root = newNode;
                return true;
            }
            Node* temp = root;
            while(true) {
                if(newNode->value == temp->value) return false;
                if(newNode->value < temp->value) {
                    if(temp->left == nullptr) {
                        temp->left = newNode;
                        return true;
                    }
                    temp = temp->left;
                } else {
                    if(temp->right == nullptr) {
                        temp->right = newNode;
                        return true;
                    }
                    temp = temp->right;
                }
            }
        }

        bool rContains(Node* currentNode, int value) {
            if(currentNode == nullptr) return false;
            if(currentNode->value == value) return true;

            if(value < currentNode->value) {
                return rContains(currentNode->left, value);
            } else {
                return rContains(currentNode->right, value);
            }
        }

        bool rContains(int value) {
            return rContains(root, value);
        }
};

int main() {
    BinarySearchTree* myBST = new BinarySearchTree();
    myBST->insert(47);
    myBST->insert(21);
    myBST->insert(76);
    myBST->insert(18);
    myBST->insert(27);
    myBST->insert(52);
    myBST->insert(82);

    cout << "\nBST Contains 27:\n";
    cout << myBST->rContains(27);

        cout << "\nBST Contains 17:\n";
    cout << myBST->rContains(17);
}
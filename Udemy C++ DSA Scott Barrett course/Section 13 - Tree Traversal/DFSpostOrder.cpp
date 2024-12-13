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

        void DFSPostOrder(Node* currentNode) {
            if(currentNode->left) {
                DFSPostOrder(currentNode->left);
            }
            if(currentNode->right) {
                DFSPostOrder(currentNode->right);
            }
            cout << currentNode->value << " ";
        }

        void DFSPostOrder() { DFSPostOrder(root); }
};
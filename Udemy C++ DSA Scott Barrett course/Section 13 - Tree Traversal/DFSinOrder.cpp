#include <iostream>

using namespace std;

class Node {
    public:
        Node* left;
        Node* right;
        int value;

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

        void DFSInOrder(Node* currentNode) {
            if(currentNode->left) {
                DFSInOrder(currentNode->left);
            }
            cout << currentNode->value << " ";
            if(currentNode->right) {
                DFSInOrder(currentNode->right);
            }
        }

        void DFSInOrder() { DFSInOrder(root); }
};
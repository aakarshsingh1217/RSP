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

        Node* rInsert(Node* currentNode, int value) {
            if(currentNode == nullptr) return new Node(value);
            if(value < currentNode->value) {
                currentNode->left = rInsert(currentNode->left, value);
            } else if(value > currentNode->value) {
                currentNode->right = rInsert(currentNode->right, value);
            }
            return currentNode;
        }

        void rInsert(int value) {
            if(root == nullptr) root = new Node(value);
            rInsert(root, value);
        }

        int minValue(Node* currentNode) {
            while(currentNode->left != nullptr) {
                currentNode = currentNode->left;
            }
            return currentNode->value;
        }

        Node* deleteNode(Node* currentNode, int value) {
            if(currentNode == nullptr) return nullptr;

            if(value < currentNode->value) {
                currentNode->left = deleteNode(currentNode->left, value);
            } else if(value > currentNode->value) {
                currentNode->right = deleteNode(currentNode->right, value);
            } else {
                if(currentNode->left == nullptr && currentNode->right == nullptr) {
                    delete(currentNode);
                    return nullptr;
                } else if(currentNode->left == nullptr) {
                    Node* temp = currentNode->right;
                    delete(currentNode);
                    return temp;
                } else if(currentNode->right == nullptr) {
                    Node* temp = currentNode->left;
                    delete(currentNode);
                    return temp;
                } else {
                    int subTreeMin = minValue(currentNode->right);
                    currentNode->value = subTreeMin;
                    currentNode->right = deleteNode(currentNode->right, subTreeMin);
                }
            }

            return currentNode;
        }

        void deleteNode(int value) {
            root = deleteNode(root, value);
        }
};

int main() {
    BinarySearchTree* myBST = new BinarySearchTree();
    myBST->rInsert(2);
    myBST->rInsert(1);
    myBST->rInsert(3);

    return 0;
};
#include <iostream>
#include <queue>

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

        void insert(int value) {
            Node* newNode = new Node(value);
            if(root == nullptr) {
                root = newNode;
                return;
            }
            Node* temp = root;
            while(true) {
                if(newNode->value == temp->value) return;
                if(newNode->value < temp->value) {
                    if(temp->left == nullptr) {
                        temp->left = newNode;
                        return;
                    }
                    temp = temp->left;
                } else {
                    if(temp->right == nullptr) {
                        temp->right = newNode;
                        return;
                    }
                    temp = temp->right;
                }
            }
        }

        void BFS() {
            queue<Node*> myQueue;
            myQueue.push(root);
            while(myQueue.size() > 0) {
                Node* currentNode = myQueue.front();
                myQueue.pop();
                cout << currentNode->value << " ";
                if(currentNode->left != nullptr) {
                    myQueue.push(currentNode->left);
                }
                if(currentNode->right != nullptr) {
                    myQueue.push(currentNode->right);
                }
            }
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

    myBST->BFS();

    return 0;
}
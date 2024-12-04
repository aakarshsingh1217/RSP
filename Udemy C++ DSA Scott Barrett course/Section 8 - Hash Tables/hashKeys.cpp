#include <iostream>
#include <vector>

using namespace std;

class Node{
    public:
        Node* next;
        string key;
        int value;

        Node(string key, int value) {
            this->key = key;
            this->value = value;
            next = nullptr;
        }
};

class HashTable {
    private:
        static const int SIZE = 7;
        Node* dataMap[SIZE];

    public:
        vector<string> keys() {
            vector<string> allKeys;
            for(int i = 0; i < SIZE; i++) {
                Node* temp = dataMap[i];
                while(temp != nullptr) {
                    allKeys.push_back(temp->key);
                    temp = temp->next;
                }
            }
            return allKeys;
        }
};
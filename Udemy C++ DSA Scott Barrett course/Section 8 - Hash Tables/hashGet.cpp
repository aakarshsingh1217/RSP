#include <iostream>

using namespace std;

class Node {
    public:
        string key;
        int value;
        Node* next;

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
            int hash(string key) {
                int hash = 0;
                for(int i = 0; i < key.length(); i++) {
                    int asciiValue = int(key[i]);
                    hash = (hash + asciiValue * 23) % SIZE;
                }
            }

            int get(string key) {
                int index = hash(key);
                Node* temp = dataMap[index];
                while(temp != nullptr) {
                    if(temp->key == key) return temp->value;
                    temp = temp->next;
                }
                return 0;
            }
};
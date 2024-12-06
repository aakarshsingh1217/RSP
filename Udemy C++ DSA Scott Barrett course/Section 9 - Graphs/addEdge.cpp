#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Graph {
    private:
        unordered_map<string, unordered_set<string>> adjList;

    public:
        bool addEdge(string vertex1, string vertex2) {
            if(adjList.count(vertex1) != 0 && adjList.count(vertex2) != 0) {
                adjList.at(vertex1).insert(vertex2);
                adjList.at(vertex2).insert(vertex1);
                return true;
            }
            return false;
        }
};
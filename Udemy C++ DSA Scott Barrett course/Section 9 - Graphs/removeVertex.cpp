#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Graph {
    private:
        unordered_map<string, unordered_set<string>> adjList;

    public:
        bool removeVertex(string vertex) {
            if(adjList.count(vertex) == 0) return false;
            for(auto otherVertex : adjList.at(vertex)) {
                adjList.at(otherVertex).erase(vertex);
            }
            adjList.erase(vertex);
            return true;
        }
};
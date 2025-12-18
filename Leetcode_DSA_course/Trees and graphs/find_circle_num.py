from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
# |->-> # Now that we built graph, let's define DFS func.
        def dfs(node):
# |         # Iterate over all neighbours in curr. node.
            for neighbour in graph[node]:
# |             # Visit nodes only if they're not seen yet
# ^             # (e.g. not in seen set).
                if (neighbour not in seen):
                    seen.add(neighbour)
                    dfs(neighbour)

# |     # Graphs given as input are more abstract.
# ^     # Typically, nodes numbered from 0 to n - 1, and you'll be
# |     # given some input where you'll have to build graph yourself.

# |     # Declare num. nodes in graph
        n = len(isConnected)
# |     # Hash map which'll map a label of a node to a list of its
# ^     # neighbours.
        graph = defaultdict(list)

# |     # Can now build this graph by iterating over all the pairs
# ^     # of labels.
        for i in range(n):
# ^         # The matrix is symmetric, isConnected[i][j] == isConnected[j][i].
# |         # If you loop over all i, j, you'd process same edge twice.
# ^         # E.g.:
# |         # isConnected =
# ^         # [
# |         #   [1, 1, 0],
# ^         #   [1, 1, 1],
# |         #   [0, 1, 1]
# ^         # ]
# |         # In above e.g., (0, 1) and (1, 0) repr. same connection.
            for j in range(i + 1, n):
                if (isConnected[i][j]):
# |                 # If connected, add edge to both lists.
                    graph[i].append(j)
                    graph[j].append(i)
# |     # Above allows us to take a label and easily find all
# ^     # neighbours.
# |
# ^     # E.g. if you have node 3 and want to find all its
# |     # neighbours, can just do:
# -<-<- # E.g. graph[3] which gives -> [..., listOfAllNeighbours].
# |
# -<-<- # When we visit a node, we'll add to seen set
        seen = set()

# ^-<-< # Now that dfs is setup, we can declare an answer and start
        # iterating over all the nodes.
        ans = 0

        for i in range(n):
            if (i not in seen):
                # If current node not in set yet, we can increment ans
                # because we found new connecting component.
                ans += 1
                # Then, add node to set and start dfs.
                seen.add(i)
                # This dfs will propogate and visit every single node in
                # connected component.
                dfs(i)

        return ans
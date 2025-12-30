class UnionFind:
    # Create a Union-Find structure with `size` elements
    def __init__(self, size):
        # Rank array stores an upper bound on the height of each tree
        self.rank = [0] * size

        # Parent array: initially, each element is its own parent
        self.parent = list(range(size))

    # Find the representative (root) of the set containing element i
    def find(self, i):
        # Get the parent of i
        root = self.parent[i]
      
        # If the parent of root is not itself, root is not the representative
        if self.parent[root] != root:
            # Recursively find the true representative and compress the path
            self.parent[i] = self.find(root)

            # Return the representative after path compression
            return self.parent[i]
      
        # If root is its own parent, it is the representative
        return root
    
    # Union the sets containing elements x and y
    def unionSets(self, x, y):
        # Find representatives of x and y
        xRoot = self.find(x)
        yRoot = self.find(y)

        # If both elements already belong to the same set, do nothing
        if xRoot == yRoot:
            return

        # Union by rank: attach the shallower tree under the deeper tree
        if self.rank[xRoot] < self.rank[yRoot]:
            # Make yRoot the parent of xRoot
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            # Make xRoot the parent of yRoot
            self.parent[yRoot] = xRoot
        else:
            # Ranks are equal: choose one root arbitrarily
            self.parent[yRoot] = xRoot

            # Increase rank because tree height may have increased
            self.rank[xRoot] += 1
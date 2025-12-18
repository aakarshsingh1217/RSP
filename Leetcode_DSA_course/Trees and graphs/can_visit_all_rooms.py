class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        def dfs(node):
            for neighbour in rooms[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        seen = { 0 }
        dfs(0)

        return len(seen) == len(rooms)
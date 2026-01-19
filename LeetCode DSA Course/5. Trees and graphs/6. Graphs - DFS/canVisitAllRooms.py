def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    seen = { 0 }

    def dfs(node: int):
        ans = 0

        for neighbour in rooms[node]:
            if neighbour not in seen:
                ans += 1
                seen.add(neighbour)
                ans += dfs(neighbour)

        return ans
    
    dfs(0)
    
    return len(seen) == len(rooms)

print(canVisitAllRooms([[1],[2],[3],[]]))
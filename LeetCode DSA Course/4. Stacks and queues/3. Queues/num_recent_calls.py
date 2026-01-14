from collections import deque

class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        while self.calls and self.calls[0] < t - 3000:
            self.calls.popleft()

        self.calls.append(t)

        return len(self.calls)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
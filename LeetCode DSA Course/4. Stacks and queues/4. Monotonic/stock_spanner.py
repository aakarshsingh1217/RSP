class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1

        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]

        self.stack.append([price, ans])

        return ans
    
obj = StockSpanner()

print("=========================")
print(obj.next(100))
print("=========================")
print(obj.next(80))
print("=========================")
print(obj.next(60))
print("=========================")
print(obj.next(70))
print("=========================")
print(obj.next(60))
print("=========================")
print(obj.next(75))
print("=========================")
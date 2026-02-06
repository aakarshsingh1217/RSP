def summing_squares(n):
  perfect_squares = []
  memo = {}

  i = 1

  while i * i <= n:
    perfect_squares.append(i * i)
    i += 1

  print(perfect_squares)

  def dp(n: int):
    if n == 0:
      return 0
    if n < 0:
      return float("inf")
    if n in memo:
      return memo[n]

    min_squares = float("inf")

    for perfect_square in perfect_squares:
      min_squares = min(min_squares, 1 + dp(n - perfect_square))

    memo[n] = min_squares

    return memo[n]

  return dp(n)
      
summing_squares(9)
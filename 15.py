def combinations(n, m):
  c = [[1] * (m + 1) for x in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      c[i][j] = c[i - 1][j] + c[i][j - 1]
  return c[n][m]
  
print(combinations(20, 20))

f_in = open('in18', 'r')
lines = f_in.readlines()
grid = []
for line in lines:
  grid.append([int(x) for x in line.split()])
ans = [[0] * (i + 1) for i in range(len(grid))]
ans[0][0] = grid[0][0]
for i in range(1, len(grid)):
  for j in range(i + 1):
    ans[i][j] = max(ans[i - 1][max(0, j - 1)], ans[i - 1][min(j, i - 1)]) + \
      grid[i][j]
print(max(ans[-1]))

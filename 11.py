f_in = open('grid11', 'r')
n = int(f_in.readline())
grid = []
for line in f_in.readlines():
  grid.append([int(x) for x in line.split()])

DIFF = [(0, 1), (1, 0), (1, 1), (1, -1)]
STEPS = 4

mx_mul = 1
for i in range(n):
  for j in range(n):
    for dx, dy in DIFF:
      mul = 1
      if 0 <= i + dx * (STEPS - 1) < n and 0 <= j + dy * (STEPS - 1) < n:
        for k in range(STEPS):
          mul *= grid[i + dx * k][j + dy * k]
      mx_mul = max(mx_mul, mul)
print(mx_mul)

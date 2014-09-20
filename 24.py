MAX_N = 10
factorial = [1] * MAX_N
for i in range(1, MAX_N):
  factorial[i] = factorial[i - 1] * i
number = 1000000 - 1
n = MAX_N - 1
perm = [0] * MAX_N
for i in range(MAX_N):
  perm[i] = number // factorial[n - i]
  number %= factorial[n - i]
used = [False] * MAX_N
for i in range(len(perm)):
  cnt = 0
  for j in range(len(used)):
    if not used[j]:
      cnt += 1
    if cnt - 1 == perm[i]:
      print(j, end='')
      used[j] = True
      break
print()

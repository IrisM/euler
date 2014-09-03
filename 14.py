def collatz(n):
  if n != 1:
    if n % 2 == 0:
      return n // 2
    else:
      return 3 * n + 1
  else:
    return n


max_num = 0
lens = [0] * (10 ** 6 + 1)
for i in range(1, 10 ** 6 + 1):
  cnt = 1
  j = collatz(i)
  while j > i:
    j = collatz(j)
    cnt += 1
  lens[i] = lens[j] + cnt
  if lens[i] > lens[max_num]:
    max_num = i
print(lens[max_num], max_num)

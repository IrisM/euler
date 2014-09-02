def erato(mx):
  lst = [True] * mx
  lst[1] = False
  for i in range(2, mx):
    if lst[i]:
      for j in range(i * i, mx, i):
        lst[j] = False
  return [i for i in range(2, mx) if lst[i]]


print(sum(erato(2 * 10 ** 6)))

def sum_fifth(n):
  sum_f = 0
  while n != 0:
    sum_f += (n % 10) ** 5
    n //= 10
  return sum_f


ans = 0
for i in range(2, 1000000):
  if sum_fifth(i) == i:
    print(i)
    ans += i
print(ans)

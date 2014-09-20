def divisors_sum(n):
  div_sum = 1
  for i in range(2, int(n ** 0.5) + 1):
    power = 0
    while n % i == 0:
      n //= i
      power += 1
    div_sum *= (i ** (power + 1) - 1) // (i - 1)
  if n != 1:
    div_sum *= n + 1
  return div_sum


ans = 0
for i in range(2, 10001):
  x = divisors_sum(i) - i
  if x != 1 and divisors_sum(x) - x == i and x != i:
    ans += i
print(ans)

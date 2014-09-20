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
  

BORDER = 28123
abundant = [False] * (BORDER + 1)
rev_ans = 0
for i in range(2, BORDER + 1):
  x = divisors_sum(i) - i
  if x > i:
    abundant[i] = True
  for j in range(12, i):
    if abundant[j] and abundant[i - j]:
      rev_ans += i
      break
print(BORDER * (BORDER + 1) // 2 - rev_ans)

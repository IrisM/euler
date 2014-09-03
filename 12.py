def prime_divisors(n):
  for i in range(2, int(n ** 0.5 + 1)):
    while n % i == 0:
      yield i
      n //= i
  if n != 1:
    yield n
    

def divisors(prime_divisors):
  divs = 1
  i = 0
  while i < len(prime_divisors):
    j = i
    while j < len(prime_divisors) - 1 and prime_divisors[j + 1] == prime_divisors[j]:
      j += 1
    divs *= j - i + 2
    i = j + 1
  return divs


for i in range(1, 2 * 10 ** 4):
  n = i * (i + 1) // 2
  divs = list(prime_divisors(n))
  if divisors(divs) > 500:
    print(i, n, divs, divisors(divs))

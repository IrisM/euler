def letters(n):
  if n <= 20:
    pre_count = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6]
    return pre_count[n]
  elif n < 100:
    pre_count = [6, 6, 5, 5, 5, 7, 6, 6]
    return pre_count[n // 10 - 2] + letters(n % 10)
  elif n < 1000:
    ans = letters(n // 100) + 7 + letters(n % 100)
    if n % 100 != 0:
      ans += 3
    return ans
  else:
    return 11
    

count = 0
for i in range(1, 1001):
  count += letters(i)
print(count)

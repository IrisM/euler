mul = 1
for i in range(2, 101):
  mul *= i
print(sum([int(x) for x in str(mul)]))

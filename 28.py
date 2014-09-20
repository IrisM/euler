MAX_N = 1001
max_num = MAX_N * MAX_N
sum_num = max_num
for i in range(MAX_N, 1, -2):
  for j in range(4):
    max_num -= i - 1
    sum_num += max_num
print(sum_num)

def next_day(cur_day):
  MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  dd, mm, yy = cur_day
  if yy % 400 == 0 or yy % 100 != 0 and yy % 4 == 0:
    MONTH_DAYS[1] += 1
  if dd + 1 <= MONTH_DAYS[mm - 1]:
    return [dd + 1, mm, yy]
  elif mm + 1 <= 12:
    return [1, mm + 1, yy]
  else:
    return [1, 1, yy + 1]



week_day = 0
cur_day = [1, 1, 1900]
while cur_day != [1, 1, 1901]:
  cur_day = next_day(cur_day)
  week_day = (week_day + 1) % 7
ans = 0
while cur_day != [31, 12, 2000]:
  if cur_day[0] == 1 and week_day == 6:
    ans += 1
  cur_day = next_day(cur_day)
  week_day = (week_day + 1) % 7
print(ans)


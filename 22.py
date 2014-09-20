f_in = open('in22', 'r')
names = f_in.readline().split("\",\"")
names[0], names[-1] = names[0][1:], names[-1][:-1]
names.sort()
print(sum([(i + 1) * sum([ord(x) - ord('A') + 1 for x in names[i]]) for i in range(len(names))]))

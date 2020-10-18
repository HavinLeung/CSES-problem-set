from sys import stdin

seq = stdin.readline()
curmax = 1
curchar = seq[0]
curcount = 1
for i in range(1, len(seq)):
  if seq[i] == curchar:
    curcount += 1
  else:
    curchar = seq[i]
    curcount = 1
  curmax = max(curmax, curcount)
print(curmax)

from sys import stdin

def solve(y,x):
  def diag(n):
    return int(n**2 - n + 1)
  bigger = max(y,x)
  mult = 1
  val = diag(bigger)
  if bigger%2 == 0:
    # going up is negative, going left is positive
    mult = 1
  else:
    # going up is positive, going left is negative
    mult = -1
  if x < bigger:
    # we're going left
    val += mult*(bigger-x)
  elif y < bigger:
    val -= mult*(bigger-y)
    # we're going up
  return val

stdin.readline()
for line in stdin:
  line = list(map(int, line.split(' ')))
  y,x = line[0], line[1]
  print(solve(y,x))
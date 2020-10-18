from math import factorial

def comb(n, k):
  k = min(k, n-k)
  run = 1
  for i in range(k):
    run *= (n-i)
  return run//factorial(k)

def trash(n):
  cur = 0
  arr = []
  for i in range(1, n+1):
    if i == 1:
      arr.append(0)
    elif i == 2:
      arr.append(6)
    elif i == 3:
      arr.append(28)
    else:
      arr.append(comb(i**2, 2) - (4*(i-3)**2 + 3*(i-3)*2 + 2*(1 + (i-2)*2) + (i-2)*2))
  return arr

def god(n):
  arr = []
  for i in range(1, n+1):
    if i == 1:
      arr.append(0)
    elif i == 2:
      arr.append(6)
    elif i == 3:
      arr.append(28)
    else:
      arr.append(comb(i**2, 2) - (4*(i-1)*(i-2)))
  return arr 

def main():
  n = int(input())
  for el in zip(trash(n), god(n)):
    assert(el[0] == el[1])
    print(el[0])

main()
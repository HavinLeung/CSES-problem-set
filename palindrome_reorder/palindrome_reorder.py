from collections import Counter
def main():
  odd = None
  lettercount = Counter(input())
  for k,v in lettercount.items():
    if v % 2 == 0:
      lettercount[k] //=2
    elif odd is None:
      odd = k*v
    else:
      print("NO SOLUTION")
      return
  if odd:
    del lettercount[odd[0]]
  s = []
  for k, v in lettercount.items():
    s.append(k*v)
  s = ''.join(s)
  print(s +('' if odd is None else odd) + s[::-1])

main()
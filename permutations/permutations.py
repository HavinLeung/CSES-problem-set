n = int(input())
if n == 1:
  print(1)
elif n in (2,3):
  print("NO SOLUTION")
else:
  def first():
    for i in range(n, 0, -2):
      print(i, end=' ')
  def second():
    for i in range(n-1, 0, -2):
      print(i, end=' ')
  if n%2==0:
    second()
    first()
  else:
    first()
    second()

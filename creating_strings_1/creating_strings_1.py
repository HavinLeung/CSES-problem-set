def dfs(cur, items, indices, arr):
  if not indices:
    arr.add(cur)
    return
  for index in indices:
    dfs(cur+items[index], items, indices.difference([index]), arr)

def main(string):
  arr = set()
  dfs("", string, set(range(len(string))), arr)
  print(len(arr))
  for item in sorted(arr):
    print(item)

main(input())
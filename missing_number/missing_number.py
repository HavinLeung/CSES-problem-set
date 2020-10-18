from sys import stdin

n = int(stdin.readline())
nums = stdin.readline().split(' ')
nums = map(int, nums)
diff = set(range(1, n+1)) - set(nums)
print(diff.pop())

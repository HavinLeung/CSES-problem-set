from sys import stdin
stdin.readline()
nums = list(map(int, stdin.readline().split(' ')))
added = 0
for i in range(1, len(nums)):
  if nums[i] < nums[i-1]:
    added += nums[i-1] - nums[i]
    nums[i] = nums[i-1]
print(added)
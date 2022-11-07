import sys

n,m = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))

low,end = 0,max(nums)

result = 0
while low <= end:
  mid = (low+end) // 2
  sum = 0
  for tree in nums :
    sum += tree-mid if tree - mid > 0 else 0
    if sum > m :
      break
  # print(f"low,mid,end,sum = {low}, {mid}, {end}, {sum}")
  if sum >= m :
    # print(mid)
    result = mid
    low = mid + 1

  else:
    sum < m
    end = mid -1

print(result)

import sys

k,n = map(int,sys.stdin.readline().split())
arr = list()

for i in range(k) :
  num = int(sys.stdin.readline().rstrip())
  arr.append(num)

low, end = 1,max(arr)

result = list()
while low <= end :
  mid = (low+end) // 2
  sum = 0
  for lan in arr :
    sum += lan // mid
  # print(f"low , mid , end = {low},{mid},{end} // {sum}")

  if sum >= n :
    # print(mid)
    result.append(mid)
    low = mid + 1

  else :
    if sum < n :
      end = mid-1

# print(result)
print(max(result))
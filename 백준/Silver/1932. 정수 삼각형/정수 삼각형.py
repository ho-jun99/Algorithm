import sys

n = int(sys.stdin.readline().strip())

arr = list()
for _ in range(n) :
  line = list(map(int,sys.stdin.readline().split()))
  arr.append(line)

for row in range(1,n):
  for col in range(len(arr[row])) :
    if col == 0 : # 시작점이면
      arr[row][col] += arr[row-1][col]
      continue
    if col == len(arr[row])-1 : # 끝점이면
      arr[row][col] += arr[row-1][col-1]
      continue
    # 그 외 경우인 경우
    arr[row][col] += max(arr[row-1][col], arr[row-1][col-1])

print(max(arr[n-1]))
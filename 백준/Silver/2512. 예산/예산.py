import sys

N = int(sys.stdin.readline()) # 지방의 수
cites = list(map(int,sys.stdin.readline().split()))
MAX = int(sys.stdin.readline()) # 최대 예산

left = 1
right = max(cites)

result = -1
while left <= right :
  mid = (left + right) // 2

  used_money = 0
  for city in cites :
    if mid <= city :
      used_money += mid
    else :
      used_money += city

  if MAX < used_money : # 돈을 더 많이 쓴 경우
    right = mid - 1
  else :
    # MAX > used_money
    left = mid + 1
    result = mid

print(result)
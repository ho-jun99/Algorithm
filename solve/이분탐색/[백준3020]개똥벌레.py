'''
  - 이분탐색을 통해서 원하는 적정 값을 찾아낸다.
'''
import sys

# 석순(밑), 종유석(위) , 석순(짝수) - 종유석(홀수) 순서

N,H = map(int, sys.stdin.readline().split()) # H = 높이
hurdles = list()
for i in range(N) :
  hurdle = int(sys.stdin.readline().strip())
  hurdles.append(hurdle)

print(hurdles)

left = 2
right = H

def search(target):
  global H
  cnt = 0

  for index,item in enumerate(target) :
    if index % 2 == 0 : # 짝수 - 밑
      if item <= target :
        cnt +=1
    else :  # 홀수 - 위
      if item <= (H-target) :
        cnt +=1
  return cnt

# 장애물 크기로 찾자.
while left <= right :
  mid = (left+ right) // 2

  cnt = search(mid)

  if cnt < mid :
    pass
  else :
    pass








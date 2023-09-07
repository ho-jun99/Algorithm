import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
dq = deque()

for i in range(N) :
  dq.append(i+1)

targets = list(map(int,sys.stdin.readline().split()))
result = 0
for target in targets :
  head = dq[0]

  # 찾아지기 때문에 별다른 조건을 걸지 않는다.
  if target == head :
    dq.popleft()
    continue
  else :
    # 아닐 경우, 왼쪽 또는 오른쪽으로 이동하는 전략을 사용해야 한다.
    dqsize = len(dq)
    mid = dqsize // 2
    targetIdx = dq.index(target)
    if mid < targetIdx :
      rotateValue = dqsize - targetIdx
      dq.rotate(rotateValue)
      result += rotateValue
    else :
      dq.rotate(-targetIdx)
      result += targetIdx

    # 하나 빼버림
    poped = dq.popleft()

print(result)

# 전체 넓이 : 10 , 찾고자하는 인덱스 8
# 전체 넓이의 절반 10 // 2 => 5 ( 여기 부터는 왼쪽으로 가는게 빠름 )
#
# 0 1 2 3 4 5 6 7 8 9
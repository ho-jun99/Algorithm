import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())

board = list()
for _ in range(N) :
  line = list(map(int,sys.stdin.readline().split()))
  board.append(line)

dirs = [
  (-1,0), (0,1), (1,0), (0,-1)
  ]


# 1 모양들 부분집합들의 크기를 미리 구해서 memo에 추가해놓는다
# 위치기록용 스택을 활용한다.
# 0에서 돌려서 memo를 활용한다
memo = [ [-1] * M for _ in range(N)]
number = 0
for row in range(N) :
  for col in range(M) :
    if board[row][col] == 1 and memo[row][col] == -1 : # 한번도 들린곳이 아니기 때문에 루틴을 수행한다.
      cnt = 1
      cur = (row, col)
      stk = deque()
      dq = deque()
      dq.append(cur)
      stk.append(cur)
      memo[row][col] = True

      while len(dq) != 0:
        now_cur = dq.popleft()

        for dir in dirs :
          next = (now_cur[0] + dir[0], now_cur[1] + dir[1])
          if 0 <= next[0] < N and 0<= next[1] < M : # 범위 안에 있고
            if memo[next[0]][next[1]] != True and board[next[0]][next[1]] == 1: # 방문했던 곳이 아니라면
              cnt +=1
              dq.append(next)
              stk.append(next)
              memo[next[0]][next[1]] = True

      while len(stk) != 0:
        now_cur = stk.pop()
        memo[now_cur[0]][now_cur[1]] = (cnt,number)
      number+=1
# print(memo)

mmax = 0
for row in range(N) :
  for col in range(M) :
    if board[row][col] == 0 :
      candidate = set()
      sum = 1
      for dir in dirs : # 4방향 돌려
        next = (row + dir[0], col + dir[1])

        if 0 <= next[0] < N and 0<= next[1] < M : # 범위 안이면
          if memo[next[0]][next[1]] != -1 :
            poped = memo[next[0]][next[1]]
            if poped[1] not in candidate : # 포함되지 않았으면
              candidate.add(poped[1])
              sum+=poped[0]
      mmax = max(mmax,sum)

print(mmax)

# ###--- BFS를 이용하는 풀이 시간초과 ---###
# mmax = 0
# # 0인곳에서 시작해서, 0의 모양을 1로 바꾸고, 최대값을 구한다.
# for row in range(N) :
#   for col in range(M) :
#     if board[row][col] == 0 :
#       visit = [ [False] * M for _ in range(N)]
#
#       dq = deque()
#       dq.append((row,col))
#       visit[row][col] = True
#
#       cnt = 1
#       while len(dq) != 0 :
#         cur = dq.popleft()
#
#         for dir in dirs :
#           next = (cur[0] + dir[0], cur[1] + dir[1])
#           if 0<= next[0] < N and 0<= next[1] < M : # 범위 안이라면
#             if visit[next[0]][next[1]] == False and board[next[0]][next[1]] == 1: # 방문하지 않았다면
#               dq.append(next) # 큐어 넣어주기
#               visit[next[0]][next[1]] = True # 방문처리
#               cnt +=1
#
#       mmax = max(mmax,cnt)
#
# print(mmax)

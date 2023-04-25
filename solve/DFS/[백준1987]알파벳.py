import copy
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

dirs = [
  (-1, 0), (0, 1), (1, 0), (0, -1)
  ]

# visit = [[True] * C for _ in range(R)] 방문처리가 필요하지 않음

board = list()
max_cnt = 0
for _ in range(R):
  line = list(sys.stdin.readline().strip())
  board.append(line)

# 방문했던 알파벳을 어떻게 관리할 것인가?
# 사용알파벳 관리
# print( ord('Z') - ord('A')) # 0 ~ 25
used = [False] * 26


def dfs(r, c, cnt):
  global max_cnt
  max_cnt = max(cnt, max_cnt)
  # print(f"({r},{c},{cnt})")

  for dir in dirs:
    next = (r + dir[0], c + dir[1])

    if 0 <= next[0] < R and 0 <= next[1] < C:
      if used[ord(board[next[0]][next[1]]) - ord('A')] == False:  # 사용하지 않았던 알파벳이라면
        used[ord(board[next[0]][next[1]]) - ord('A')] = True
        dfs(next[0], next[1], cnt + 1)
        used[ord(board[next[0]][next[1]]) - ord('A')] = False

used[ord(board[0][0]) - ord('A')] = True # 초기 시작점은 항상 사용됨
dfs(0, 0, 1)
print(max_cnt)

# ##### ------ 시간초과 풀이 ------ #####
# stk = deque()
# stk.append((0, 0, [],1))  # ( row, col, 방문했던 알파벳 )
#
# while len(stk) != 0 :
#   cur = stk.pop()
#   max_cnt = max(max_cnt,cur[3])
#
#   for dir in dirs :
#     next_list = copy.deepcopy(cur[2])
#     next_list.append(board[cur[0]][cur[1]])
#     next = ( cur[0] + dir[0], cur[1] + dir[1], next_list, cur[3] + 1 )
#
#     if 0 <= next[0] < R and 0<= next[1] < C : # 범위 체크
#         if board[next[0]][next[1]] not in next[2] : # 중복되는 알파벳이 없다면
#           stk.append(next) # 스택에 넣어주고
#
#
# print(max_cnt)
# ##### ------------------------ #####

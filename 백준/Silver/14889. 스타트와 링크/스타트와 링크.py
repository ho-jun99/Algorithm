import sys

N = int(sys.stdin.readline().strip())
board = list()

for _ in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  board.append(line)

visit = [False] * N
per_team = N // 2

mmin = float('inf')
# print(board)


def seperate(cur, depth):
  global visit, mmin, per_team, N
  if depth == per_team:
    teamA, teamB = 0, 0
    for i in range(N):
      for j in range(i, N):  # 절반만 돌려버리자
        if visit[i] and visit[j]:
          teamA += board[i][j] + board[j][i]
        elif not visit[i] and not visit[j]:
          teamB += board[i][j] + board[j][i]
    mmin = min(mmin, abs(teamA - teamB))
    if mmin == 0 :
      print(mmin)
      exit()
    # print(visit)
    return
  for person in range(cur, N):
    if not visit[person]:
      visit[person] = True
      seperate(person + 1, depth + 1)
      visit[person] = False


seperate(0, 0)
print(mmin)

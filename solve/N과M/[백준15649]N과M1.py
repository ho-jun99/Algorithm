import sys
from itertools import permutations

N,M = map(int,sys.stdin.readline().split())
targets = [i for i in range(1,N+1)]
# # print(targets)
#
# 중복없이 M개를 고른 수열
#   조합을 사용한다.
# for permu in permutations(targets,M) :
#   print(*permu)



# 순열 -> 백트래킹을 활용하는 방법
visit = [False] * (N+1)
def dfs(node ,length) :
  global visit
  global M

  if M <= length :
    print(node)
    return

  for target in targets :
    if visit[target] == False :
      visit[target] = True
      next = node + " " + str(target)
      dfs(next,length+1)
      visit[target] = False

for i in range(1,N+1) :
  visit[i] = True
  dfs(str(i),1)
  visit[i] = False
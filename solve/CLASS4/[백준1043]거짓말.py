import sys
from collections import defaultdict
from collections import deque

def print2D(arr):
  for a in arr :
    print(a)

# 사람의 수 N, 파티의 수 M
N,M = map(int,sys.stdin.readline().split())

# 진실을 아는 사람의 수, 0번인덱스는 총 크기
trues = list(map(int,sys.stdin.readline().split()))
if trues[0] > 0 :
  trues = trues[1:]

parties = list()
d = defaultdict(list)
for i in range(M) :
  party = list(map(int,sys.stdin.readline().split()))[1:]
  parties.append(party)
  for p in party :
    d[p].append(i)

visit_party = [True] * M # 파티 만큼
visit_person = [False] * (N+1) # 사람 수 만큼

# 그래프 탐색처럼 해보자!
dq = deque()

for true in trues :
  dq.append(true) # 사람을 넣는다. 사람을 기준으로 파티를 찾고 순회할 예정이다.

while len(dq) != 0 :
  poped = dq.popleft()
  visit_person[poped] = True # 방문처리 한다.

  for party_idx in d[poped] :
    if visit_party[party_idx] == False :
      continue
    else :
      visit_party[party_idx] = False

      for person in parties[party_idx] :
        if visit_person[person] == False :
          dq.append(person)

# print(visit_party)
# print(visit_person)

sum = 0
for result in visit_party :
  if result == True :
    sum += 1

print(sum)
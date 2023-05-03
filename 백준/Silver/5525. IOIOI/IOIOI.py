import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

# print(n,m,s)


# P_n이 주어진다
# P_n의 갯수를 찾으면 된다
# 파이썬 문자열의 find를 활용한다면?


Pn = ""

for i in range(n+1) :
  if i== n :
    Pn += "I"
  else :
    Pn += "IO"

cursor = 0
cnt = 0
result = 0
while cursor < m-2 :
  if s[cursor:cursor+3] == "IOI" :
    cursor +=2
    cnt +=1
    if cnt == n :
      result +=1
      cnt -=1
  else :
    cursor += 1
    cnt = 0

print(result)

def solve50_same1() :
  # 순회 한번으로 IOI의 총 갯수를 구함
  cursor = 0
  cnt = 0
  result = 0
  while cursor < m - 2 :
    if s[cursor:cursor+3] == "IOI" :
      cursor += 2
      cnt +=1
      if cnt == n :
        result+=1
        cursor = cursor - (2*n) + 1
        cnt = 0
    else :
      cnt = 0
      cursor +=1
  print(result)

# IOI는 모든 Pn에 포함 된 수이고, n으로 나누어버린다.



def solve50point():
  # print(Pn)
  start = 0
  cnt = 0
  while s.find(Pn,start) != -1:
    cnt +=1
    start = s.find(Pn,start) +1
    # print(f"index : {start-1}")
  print(cnt)
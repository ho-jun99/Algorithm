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

# print(Pn)
start = 0
cnt = 0
while s.find(Pn,start) != -1:
  cnt +=1
  start = s.find(Pn,start) +1
  # print(f"index : {start-1}")
print(cnt)
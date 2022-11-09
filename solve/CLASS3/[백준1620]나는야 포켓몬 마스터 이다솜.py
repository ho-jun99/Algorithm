import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
# n 도감에 수록된 포켓몬의 개수
# m 내가 맞춰야 하는 문제의 개수
# isdigit

mylist = list()
cnt = 1
int_to_str = dict()
str_to_int = dict()
for _ in range(n):
  pocketmon = sys.stdin.readline().rstrip()
  int_to_str[cnt] = pocketmon
  str_to_int[pocketmon] = cnt
  cnt+=1

for i in range(m) :
  a = sys.stdin.readline().rstrip()
  if a.isdigit():
    print(int_to_str[int(a)])
  else :
    print(str_to_int[a])


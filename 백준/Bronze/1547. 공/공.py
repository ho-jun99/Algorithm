import sys


t = int(sys.stdin.readline())
cups = [1,2,3]
def swap(a,b) :
  global cups
  temp = cups[a]
  cups[a] = cups[b]
  cups[b] = temp
  # print(cups)


for _ in range(t) :
  a,b = map(int,sys.stdin.readline().split())
  swap(a-1,b-1)

print(cups.index(1)+1)

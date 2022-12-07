import sys


def unsolve() :
  m,n,x,y = map(int,sys.stdin.readline().split())
  iterX = 1; iterY = 1;
  year = 1

  while not (iterX == x and iterY == y) :
    year +=1
    if iterX < m :
      iterX+=1
    else :
      iterX = 1
    if iterY < n :
      iterY +=1
    else :
      iterY = 1
    # print(year, iterX, iterY)
    if iterX == m and iterY == n:
      print(-1)
      return
  print(year)



def solve() :
  m, n, x, y = map(int, sys.stdin.readline().split())
  k = x
  while k <= m * n:
    if (k - x) % m == 0 and (k - y) % n == 0:
      return k
    k += m
  return -1


t = int(sys.stdin.readline())
for i in range(t) :
  print(solve())
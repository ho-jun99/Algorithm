import sys

# 시간초과 풀이
def solve(h,w,n) :
  list = [[False for j in range( n//h +1 )] for i in range(h)]
  memo = [0,0]

  for i in range(n) :
    for col in range(n//h + 1) :
      isUpdate = False
      for row in range(h) :
        if list[row][col] :
          continue
        else:
          list[row][col] = True
          isUpdate = True
          if( i== n-1) :
            memo[0] = row+1
            memo[1] = col+1
          break
      if isUpdate :
        break

  for i in range(h) :
    print(list[i])
  print(memo[0],end="")
  print(str(memo[1]).rjust(len(str(max(w,10))),"0"))


def solve2(h,w,n) :
  col = n//h if n % h == 0 else (n // h)+1
  row = h if n % h == 0  else n%h
  # print(row,end="")
  # print(str(col).rjust(len(str(max(w,10))),"0"))
  print(f'{row}{str(col).rjust(len(str(max(w,10))),"0")}')

t = int(input())
for i in range(t) :
  h,w,n = map(int, sys.stdin.readline().split())
  solve2(h,w,n)


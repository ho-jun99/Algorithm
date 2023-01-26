import sys

# R 뒤집기 -> 순서를 뒤집는 함수
# D 버리기 -> 첫번째 수를 버리는 함수

def solve():
  p = sys.stdin.readline().strip()
  n = int(sys.stdin.readline())
  arr = eval(sys.stdin.readline())
  start = 0
  last = 0 if n == 0 else n-1
  isFoward = True

  for command in p :
    if command == "R":
      isFoward = not isFoward

    else:
      n-=1
      if n < 0 :
        print("error")
        return
      if isFoward :
        start += 1
      else :
        last -= 1

  if start == last :
    if n == 0 :
      print("[]")
    else :
      print("[" + str(arr[start]) + "]" )
  else :
    print("[",end="")
    if isFoward:
      for i in range(start,last+1):
        if i == last :
          print(arr[i], end="")
        else :
          print(arr[i],end=",")
    else :
      for i in range(last,start-1,-1):
        if i == start :
          print(arr[i],end="")
        else :
          print(arr[i],end=",")
    print("]")

T = int(sys.stdin.readline())
for i in range(T):
  solve()
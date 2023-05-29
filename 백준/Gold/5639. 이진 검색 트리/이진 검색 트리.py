import sys
sys.setrecursionlimit(10**6)
def printSolve(arr) :
  for i in arr :
    print(i)

# 몇개인지 모르는걸 입력받을때는 아래와 같이 수행하자.
bst = list()
while True :
  try :
    bst.append(int(sys.stdin.readline().strip()))
  except :
    break

l = 0
r = len(bst)-1
result = list()
def sub(l,r) :
  global result,bst

  if l == r :
    result.append(bst[r])
    return

  if l > r :
    return

  root = bst[l]
  mid = l
  for i in range(l+1,r+1) :
    if root < bst[i] :
      mid = i
      break

  # print(f"root : {root} , l: {l},mid : {mid} r : {r} , result : {result}")
  if mid == l : # 큰거를 찾지 못했을때
    sub(l+1,r)
  else :
    # 여기서 mid가 발견되지 않을 경우 처리해야 할듯?
    sub(l+1,mid-1)
    sub(mid,r)
  result.append(root)

sub(l,r)
printSolve(result)
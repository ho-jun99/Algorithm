import sys

sys.setrecursionlimit(100_000)

n = int(sys.stdin.readline().strip())
inorders = list(map(int,sys.stdin.readline().split()))
postorders = list(map(int,sys.stdin.readline().split()))



# 1. postorder를 통해서 ROOT노드를 알 수 있다.
  # - 맨 끝 노드가 ROOT 임
# 2. inorder에서 위에서 찾은 ROOT를 찾고 L,R로 쪼갤 수 있다.
  # - inorder에서 오른쪽으로 개수를 센다
  # - 센 개수만큼을 post의 현재 root_index에서 빼준다
  # - 새로운 루트를 발견한다.

result = list()
def inorder(l,r,target) :
  global inorders
  idx = inorders.index(target)
  return (idx-l,r-idx,idx) # 루트에서 왼쪽의 lefa 개수, 오른쪽의 leaf 개수, 현재 위치

call_cnt = 0
def solve(l,r,inorder_l,inorder_r) :
  global postorders,result,call_cnt
  call_cnt+=1
  if l > r :
    return
  target = postorders[r]
  result.append(target)
  left_cnt,right_cnt,inorder_root_idx = inorder(inorder_l,inorder_r,target)
  # print(f"{result} l : {l} , r: {r} , inorder_l : {inorder_l}, inorder_r : {inorder_r}")

  solve(l,l+left_cnt-1, inorder_l,inorder_root_idx-1) # 왼쪽
  solve(l+left_cnt,r-1,inorder_root_idx+1,inorder_r) # 오른쪽

solve(0,n-1,0,n-1)
print(*result)
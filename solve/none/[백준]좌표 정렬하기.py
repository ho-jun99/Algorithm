import sys


# key를 이용한 다중조건 정렬
# x[0]에 대해서 정렬한 후 x[0]에 대한 조건이 같으면
# x[1]에 대한 조건을 통해서 정렬해줌
def solve():
  N = int(input())
  arr = []
  for _ in range(N):
    x,y = sys.stdin.readline().strip().split()
    data = (int(x),int(y))
    arr.append(data)
  arr.sort(key=lambda x:(x[0],x[1]))
  for item in arr:
    print(item[0],item[1])

# 그냥 정렬을 해도 튜플의 인덱스를 비교해서 정렬해줌
def solve2():
  N = int(input())
  arr = []
  for _ in range(N):
    x,y = sys.stdin.readline().strip().split()
    data = (int(x),int(y))
    arr.append(data)
  arr.sort()
  for item in arr:
    print(item[0],item[1])

if __name__ == '__main__':
    solve()

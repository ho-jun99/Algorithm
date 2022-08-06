"""
  그냥 풀 경우 메모리 제한에 걸리게 됨
  그 이유는 천만개의 데이터가 들어올 수 있는데
  천만개에 해당하는 모든 데이터를 배열에 넣게되면 메모리를 초과 할수 밖에 없음
  배열에 모든 수를 담지 않고 계산할 수 있는 방법을 찾아야 함.
  계수 정렬을 사용행함
"""

# 아래 방법은 조금 비효율 적임. 굳이 딕셔너리를 사용하지 않고 배열의 인덱스를 map처럼 사용하면 됨
import sys


def not_solve():
  N = int(input())
  data = dict()
  arr = []
  for _ in range(N):
    num = int(input())
    if num not in data:
      data[num] = 1
      arr.append(num)
    else :
      data[num] += 1

  arr.sort()

  for i in arr:
    for _ in range(data[i]):
      print(i)

# 아래를 계수정렬이라고 함
def solve():
  N = int(input())
  arr = [0] * 10_001
  for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

  for i in range(10_001):
    if arr[i] == 0:
      continue
    for j in range(arr[i]):
      print(i)


if __name__ == '__main__':
    solve()
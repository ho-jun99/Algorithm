"""
  다른 풀이전략.
  간단하게 sort후 비교해도 되지만, 원소가 많아지는 경우에는 불리
  오름차순, 내림차순은 두개의 원소만 비교하면 알 수 있음
  오름차순, 내림차순 두개의 플레그를 설정하고, 비교해가면서 각 플래그의 조건을 만족하지 못하면 False로설정
  두개다 False일 경우는 mixed임
"""
import sys

ASCENDING = "ascending"
DECENDING = "descending"
MIXED = "mixed"

def solve(data):
  sorted_data = sorted(data)
  reversed_data = sorted(data,reverse=True)

  if data == sorted_data:
    return ASCENDING
  elif data == reversed_data:
    return DECENDING
  else:
    return MIXED


if __name__ == '__main__':
  input = list(map(int,sys.stdin.readline().strip().split()))
  answer = solve(input)
  print(answer)

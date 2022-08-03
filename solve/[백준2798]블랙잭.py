"""
  파이썬은 1초에 대략 2천만번 연산을 수행
  조합공식을 이용했을때 최대 100만가지밖에 안되기 때문에 3중반복문으로 모든 경우의 수를 더하면 됨
"""
import sys

def solve(N,M,cards):
  size_card = len(cards)
  max = 0

  for i in range(size_card):
    for j in range(i+1,size_card):
      for k in range(j+1,size_card):
        check = cards[i] + cards[j] + cards[k]
        if check > max and check <= M:
          max = check
  return max


if __name__ == '__main__':
  N,M = list(map(int,sys.stdin.readline().strip().split()))
  cards = sorted(list(map(int,sys.stdin.readline().strip().split())),reverse=True)
  answer = solve(N,M,cards)
  print(answer)

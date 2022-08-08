"""
  find는 찾지 못하면 -1 반환, index함수는 에러 반환
  find ( 찾을문자열 ) or
  find( 찾을문자열, 시작위치 ) or
  find( 찾을문자열, 시작위치, 종료위치)
"""
import sys

def solve():
  case = sys.stdin.readline().strip()
  target = sys.stdin.readline().strip()
  cnt = 0

  idx = 0
  while True:
    place = case.find(target,idx)
    if place == -1 :
      break
    else :
      idx = place + len(target)
      cnt += 1

  print(cnt)

if __name__ == '__main__':
  solve()

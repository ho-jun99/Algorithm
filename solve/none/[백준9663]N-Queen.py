'''
  수직체크, 수평체크, 대각선 체크가 필요
  백트레킹기법을 사용해서, 조건에 맞지 않으면 그 뒤는 탐색할 필요가 없음
'''
import sys

cnt = 0

def is_available(row, col, info):
  # 들어온 row와 col에 대한 수직검사, 수평검사

  # 수직검사
  # for i in info:
  #   if col == i:
  #     return False

  # 대각 검사 + 대각검사
  for queen_row, queen_col in enumerate(info):
    if col == queen_col or abs(col - queen_col) == abs(row-queen_row):
      return False

  return True


def back_tracking(N, upper_queen_info, result):
  cur_row = len(upper_queen_info)

  # 재귀 함수 종료조건 작성
  if cur_row == N:
    # result.append(upper_queen_info[:])
    global cnt
    cnt +=1
    return

  for candidate_col in range(N):
    if is_available(cur_row, candidate_col, upper_queen_info):
      upper_queen_info.append(candidate_col)
      back_tracking(N, upper_queen_info, result)
      upper_queen_info.pop()

  return


def answer(N):
  result = []
  for first_col in range(N):
    list_strat = [first_col]
    back_tracking(N, list_strat, result)
  return result


if __name__ == '__main__':
  N = int(sys.stdin.readline().strip())
  a = answer(N)
  # print(a)
  print(cnt)

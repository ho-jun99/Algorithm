import sys

# 시험장 수
N = int(sys.stdin.readline())
# 시험장별 응시인원
arrs = list(map(int,sys.stdin.readline().split()))
# 총 감독관이 감시할 수 있는 응시자, 부 감독관이 감시할 수 있는 응시자
B,C = map(int,sys.stdin.readline().split())

# 필요한 감독간 수의 최솟값을 구하시오
bp = 0
cp = 0

for arr in arrs :
  arr -= B
  bp +=1
  if arr > 0 :
    cp += arr // C
    if arr % C != 0 :
      cp +=1

print(bp+cp)

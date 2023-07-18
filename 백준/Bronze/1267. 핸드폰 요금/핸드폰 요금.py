import sys

N = int(sys.stdin.readline())
arrs = map(int,sys.stdin.readline().split())
# 영식(Y) 30초마다 10원
# 민식(M) 60초마다 15원
yd = 30
md = 60
y = 0
m = 0
for arr in arrs:
  y += arr // yd
  m += arr // md
  if arr % yd >= 0 :
    y += 1
  if arr % md >= 0 :
    m += 1

y = y*10
m = m*15
# print(y,m)
if y > m :
  print("M", m)
elif y < m :
  print("Y", y)
else :
  print("Y M",y)


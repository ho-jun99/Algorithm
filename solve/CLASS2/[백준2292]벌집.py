n = int(input())

if n == 1 :
  print(1)
  exit()

# 1, 6, 12, 18, 24 ...
step = 0
cnt = 0
while n > 1 :
  n = n - step
  step += 6
  cnt+=1



print(cnt)
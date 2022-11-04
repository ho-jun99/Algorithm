target = int(input())

if target == 1:
  print(0)
  exit()

for i in range(1,target) :
  copy = i
  sub_sum = 0

  while copy // 10 != 0 :
    sub_sum += copy % 10
    copy = copy // 10
  sub_sum += copy

  if( i + sub_sum == target) :
    print(i)
    break

  if( i == target-1) :
    print(0)
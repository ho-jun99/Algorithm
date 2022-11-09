n = int(input())

f = 1
cnt = 0
for i in range(n,1,-1) :
  f *= i
# print(f)

while f%10 == 0 :
  cnt+=1
  f = f//10

print(cnt)
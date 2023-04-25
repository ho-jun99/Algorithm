import sys

# start at 100

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if m == 0 :
  b = list()
else :
  b = list(sys.stdin.readline().strip().split())



check = abs(100-n)
iter = -1
while True :
  # plus
  iter+=1
  pflag = True
  mflag = True
  for broken in b :
    if broken in str(n+iter) :
      pflag= False
    if broken in str(n-iter) :
      mflag= False

  if check < len(str(n+iter)) + abs(n - (n+iter)) or check < len(str(n-iter)) + abs(n - (n+iter)) :
    print(check)
    break

  result = float('inf')
  result2 = float('inf')

  if pflag or mflag:
    if pflag :
      result = len(str(n+iter)) + abs(n - (n+iter))
    if mflag :
      result2 = len(str(n - iter)) + abs(n - (n + iter))
    print(min(result,result2,check))
    break





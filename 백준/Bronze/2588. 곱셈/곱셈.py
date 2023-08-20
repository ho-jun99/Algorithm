import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
strB = str(b)
for i in range(len(strB)) :
  print(a * (int(strB[len(strB)-1-i])))
print(a*b)



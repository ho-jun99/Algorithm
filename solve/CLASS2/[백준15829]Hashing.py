import sys

r = 31
m = 1234567891
base = 96

l = int(input())
str = input()

sum = 0
for i in range(len(str)) :
  sum += (ord(str[i])-base) * r**(i)

print(sum % m)




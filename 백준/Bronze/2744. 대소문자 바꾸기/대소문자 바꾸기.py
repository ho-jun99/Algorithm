import sys

arrs = list(sys.stdin.readline().strip())

# print(arrs)

result = ""
for arr in arrs :
  if str(arr).isupper() :
    result += str(arr).lower()
  else :
    result += str(arr).upper()

print(result)
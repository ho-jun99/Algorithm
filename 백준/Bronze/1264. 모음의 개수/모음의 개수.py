import sys

while True :
  arrs = list(sys.stdin.readline().strip())
  if len(arrs) == 1 and arrs[0] == '#' :
    break
  sum = 0
  for arr in arrs :
    if arr =='a' or arr == 'e' or arr == 'i' or arr == 'o' or arr == 'u' :
      sum +=1
    if arr == 'A' or arr == 'E' or arr == 'I' or arr == 'O' or arr == 'U':
      sum +=1
  print(sum)

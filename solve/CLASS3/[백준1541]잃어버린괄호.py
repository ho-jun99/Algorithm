import sys

mstr = sys.stdin.readline().strip()

arr = list()
num = ""
for i in range(len(mstr)):
  if i == len(mstr) - 1 :
    num += mstr[i]
    arr.append(num)
  if mstr[i] == "+" or mstr[i] == "-" :
    arr.append(num)
    arr.append(mstr[i])
    num = ""
  else :
    num += mstr[i]

result = ""
isOpen = False
for i in range(len(arr)) :
  if arr[i] == "-" :
    if not isOpen :
      result += "-("
      isOpen = True
    else :
      result += ")-("
      isOpen = True
  elif arr[i] == "+" :
    result += "+"
  else :
    if isOpen and i == len(arr)-1 :
      result += f"{str(int(arr[i]))})"
    else :
      result += str(int(arr[i]))
# print(result)
print(eval(result))
while True :
  n = input()
  if n == "0" : break
  left = 0
  right = len(n)-1

  while True :
    if left >= right :
      print("yes")
      break
    if n[left] == n[right] :
      left+=1
      right-=1
      continue
    else :
      print("no")
      break



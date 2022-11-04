n = int(input())
arr = [i for i in range(1,n+1)]

iter=0
while iter < len(arr)-1:
  iter +=1
  arr.append(arr[iter])
  iter +=1


print(arr[len(arr)-1])
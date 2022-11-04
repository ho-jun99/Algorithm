import sys

t = int(input())
arr = list()

for _ in range(t) :
  w,h = map(int,sys.stdin.readline().split())
  arr.append((w,h))

for i in range(len(arr)):
  rank = 1
  pivot = arr[i]
  for j in range(len(arr)) :
    if i==j : continue
    iterate = arr[j]
    if (pivot[0] < iterate[0]) and (pivot[1] < iterate[1]) :
      rank +=1

  print(rank, end=" ")

# print(arr)
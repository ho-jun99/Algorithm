import random


def merge(left, right):
  sorted = []
  lptr, rptr = 0, 0
  while lptr < len(left) and rptr < len(right):
    if left[lptr] < right[rptr]:
      sorted.append(left[lptr])
      lptr += 1
    else:
      sorted.append(right[rptr])
      rptr += 1

  if( lptr < len(left)) :
    for i in range(lptr,len(left)) :
      sorted.append(left[i])
  elif ( rptr < len(right)) :
    for i in range(rptr, len(right)):
      sorted.append(right[i])
  print(f"merge {sorted}")
  return sorted

def merge_sort(data) :
  print("merge_sort called")
  if len(data) <= 1:
    return data
  pivot = len(data) // 2
  left = merge_sort(data[:pivot])
  right = merge_sort(data[pivot:])
  print(left,right)
  return merge(left,right)

if __name__ == '__main__':
  sample = [4, 3, 7, 2, 6, 8, 9, 0, 1, 5]
  answer = merge_sort(sample)
  print(f"sorted : {answer}")

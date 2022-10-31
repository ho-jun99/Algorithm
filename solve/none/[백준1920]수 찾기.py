from sys import stdin, stdout

def answer(data, target,left,right):
  mid = (left + right) // 2
  if left > right :
    return False

  if data[mid] == target :
    return True
  elif target < data[mid] :
    return answer(data,target,left,mid-1)
  elif target > data[mid] :
    return answer(data,target,mid+1,right)

if __name__ == '__main__':
  n = stdin.readline()
  N = sorted(map(int, stdin.readline().split()))
  m = stdin.readline()
  M = map(int, stdin.readline().split())

  for target in M :
    if answer(N, target, 0, len(N)-1) :
      print(1)
    else:
      print(0)


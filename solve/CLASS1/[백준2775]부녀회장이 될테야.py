



def solve():
  r = int(input())
  n = int(input())
  arr = [ [0 for j in range(0,n+1)] for i in range(r+1)]
  arr[0] = [i for i in range(0,n+1)]

  for i in range(1,r+1):
    for j in range(n+1):
      for k in range(j+1):
        arr[i][j] += arr[i-1][k]

  print(arr[r][n])

if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    solve()

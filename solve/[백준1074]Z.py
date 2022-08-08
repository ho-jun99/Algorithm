import sys

def z(n,row,col):
  if n == 1:
    if row == 0 and col == 0 :
      return 0
    if row == 0 and col == 1 :
      return 1
    if row == 1 and col == 0 :
      return 2
    if row == 1 and col == 1 :
      return 3
  before_size = 2**(n-1)

  if row < before_size and col < before_size :
    count = 0
    # print(f"제 0사분면 {n}, {row}, {col}")
  elif row < before_size and col >= before_size :
    count = 1
    col -= before_size
    # print(f"제 1사분면 {n}, {row}, {col}")
  elif row >= before_size and col < before_size :
    count = 2
    row -= before_size
    # print(f"제 2사분면 {n}, {row}, {col}")
  else :
    count = 3
    row -= before_size
    col -= before_size
    # print(f"제 3사분면 {n}, {row}, {col}")
  return (count*before_size**2) + z(n-1,row,col)

def solve():
  n,row,col = map(int,sys.stdin.readline().strip().split())
  answer = z(n,row,col)
  print(answer)

if __name__ == '__main__':
    solve()

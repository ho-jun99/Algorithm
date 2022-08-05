import hashlib

def solve(str):
  print(hashlib.sha256(str.encode()).hexdigest())

if __name__ == '__main__':
  S = input()
  solve(S)
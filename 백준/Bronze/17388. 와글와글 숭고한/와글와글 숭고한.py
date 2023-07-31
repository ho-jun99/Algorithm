import sys

S,K,H = map(int,sys.stdin.readline().split())


if S+K+H >= 100 :
  print('OK')
elif min(S,K,H) == S :
  print("Soongsil")
elif min(S,K,H) == K :
  print("Korea")
else :
  print("Hanyang")


import sys

a = map(int,sys.stdin.readline().split())
b = map(int,sys.stdin.readline().split())

print(max(sum(a),sum(b)))
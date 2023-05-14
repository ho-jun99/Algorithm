import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
graph = defaultdict(lambda : defaultdict(str))
LEFT = 1
RIGHT = -1

for _ in range(N) :
  parent, left, right = sys.stdin.readline().split()
  if left != "." :
    graph[parent][LEFT] = left
  if right != "." :
    graph[parent][RIGHT] = right

def left(node) :
  return graph[node][LEFT]

def right(node) :
  return graph[node][RIGHT]

def preorder(cur) :
  l = left(cur)
  r = right(cur)
  # ----------- #

  print(cur,end="")
  if l != "" :
    preorder(l)

  if r != "" :
    preorder(r)

def inoredr(cur) :
  l = left(cur)
  r = right(cur)
  # ----------- #


  if l != "":
    inoredr(l)
  print(cur,end="")
  if r != "":
    inoredr(r)

def postorder(cur) :
  l = left(cur)
  r = right(cur)
  # ----------- #

  if l != "":
    postorder(l)
  if r != "":
    postorder(r)
  print(cur, end="")

preorder("A")
print()
inoredr("A")
print()
postorder("A")


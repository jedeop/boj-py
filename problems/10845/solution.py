import collections
import sys

stack = collections.deque()

n = int(sys.stdin.readline().strip())
for _ in range(n):
  args = sys.stdin.readline().strip()
  if args == "pop":
    try:
      print(stack.popleft())
    except IndexError:
      print(-1)
  elif args == "size":
    print(len(stack))
  elif args == "empty":
    if stack:
      print(0)
    else:
      print(1)
  elif args == "back":
    try:
      last = stack.pop()
      stack.append(last)
      print(last)
    except IndexError:
      print(-1)
  elif args == "front":
    try:
      print(stack[0])
    except IndexError:
      print(-1)
  else:
    args = args.split(" ")
    stack.append(args[1])

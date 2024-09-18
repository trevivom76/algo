import sys
N = int(input())

stack = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        print(stack.pop() if stack else -1)
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        print(1 if not stack else 0)
    elif a[0] == 5:
        print(stack[-1] if stack else -1)

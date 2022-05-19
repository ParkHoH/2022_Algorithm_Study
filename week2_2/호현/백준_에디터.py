import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []
M = int(input())

for _ in range(M):
    command = input().rstrip()
    if command == "L":
        if stack1: stack2.append(stack1.pop())
    elif command == "D":
        if stack2: stack1.append(stack2.pop())
    elif command == "B":
        if stack1: stack1.pop()
    else:
        stack1.append(command[2])

print(''.join(stack1+stack2[::-1]))
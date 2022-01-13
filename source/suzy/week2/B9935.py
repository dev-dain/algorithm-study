import sys
s = list(sys.stdin.readline().rstrip())
e = list(sys.stdin.readline().rstrip())

stack = []

for i in range(len(s)):
    stack.append(s[i])
    if stack[-1] == e[-1] and len(stack) >= len(e):
        if stack[-len(e):] == e:
            for i in range(len(e)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")        


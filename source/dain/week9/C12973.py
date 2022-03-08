# 9935와 비슷
def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
            continue
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return 0 if stack else 1
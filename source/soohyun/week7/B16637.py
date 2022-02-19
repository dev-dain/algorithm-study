# 백준 16637 괄호 추가하기
# https://www.acmicpc.net/problem/16637

n = int(input())
exp = input()
num, op = [], [] # 수식의 숫자, 연산자 리스트
ans = -1e9 # 최대값

for e in exp:
    num.append(e) if e.isdigit() else op.append(e)

def dfs(idx, total):
    global ans

    # 수식 계산이 끝나면 최대값을 구하고 리턴
    if idx == len(op):
        ans = max(ans, int(total))
        return

    # 현재 연산자에서 괄호 넣기
    # (3+8)×7-9×2
    first = str(eval(total + op[idx] + num[idx+1]))
    dfs(idx+1, first)

    # 다음 연산자에서 괄호 넣기
    # 3+(8x7)-9×2
    if idx + 1 < len(op):
        next = str(eval(num[idx+1] + op[idx+1] + num[idx+2])) # 괄호 값 계산
        second = str(eval(total + op[idx] + next))
        dfs(idx+2, second)

dfs(0, num[0])
print(ans)
import sys
input = sys.stdin.readline

n = int(input())
m = input()

# 각 연산자 계산
def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

max_sum = float('-inf')
# 완전탐색
def dfs(idx, ans):
    global max_sum
    if idx >= len(opr):
        max_sum = max(max_sum, ans)
        return
    
    dfs(idx+1, cal(ans,num[idx+1],opr[idx]))
    
    # 괄호가 뒤에 존재하는 경우
    if idx+1 < len(opr):
        dfs(idx+2, cal(ans, cal(num[idx+1],num[idx+2],opr[idx+1]), opr[idx]))
        
num,opr = [], []
def sol(m):
    # 숫자와 연산자 분리
    for i in m[:-1]:
        if i.isdigit():
            num.append(int(i))
        else:
            opr.append(i)
    dfs(0, num[0])
sol(m)
print(max_sum)
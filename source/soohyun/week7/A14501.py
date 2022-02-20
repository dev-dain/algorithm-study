# 백준 14501 퇴사
# https://www.acmicpc.net/problem/14501


n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if schedule[i][0] + i > n: # 현재 일자에 상담을 할 수 없는 경우
        dp[i] = dp[i+1] # 현재 수익 = 다음날 수익 
    else: # 현재 일자에 상담을 할 수 있는 경우 
        dp[i] = max(dp[i+1], schedule[i][1] + dp[schedule[i][0] + i]) # 현재 일자에 상담을 안하고 다음날 수익과 같은 경우, 현재 일자에 상담을 해서 수익을 얻는 경우 중 최대값을 저장

print(dp[0])
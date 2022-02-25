from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*n for _ in range(n)] for _ in range(3)] # 가로 0 세로 1 대각선 2
dp[0][0][1] = 1

i = 2
while i < n:
    if home[0][i]:
        break
    dp[0][0][i] = 1
    i += 1
    
for i in range(1,n):
    for j in range(2,n):
        # 대각선은 총 두 칸
        if home[i][j] ==0 and home[i][j-1] == 0 and home[i-1][j] == 0:
            dp[2][i][j] = sum(dp[k][i-1][j-1] for k in range(3))
        # 가로나 세로일 경우 한칸만 비어있으면 가능
        if home[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
# dp 를 돌며 
print(sum(dp[i][-1][-1] for i in range(3)))
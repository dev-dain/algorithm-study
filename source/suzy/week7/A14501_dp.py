# dp 풀이
n = int(input())

# t 완료하는 기간 p 이익
t = []
p = []
dp = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)    

for i in range(n-1,-1,-1):
    if t[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+dp[i + t[i]])
print(dp[0])
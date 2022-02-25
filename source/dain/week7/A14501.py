N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]
dp = [p for (_, p) in consult] + [0]
for i in range(N-1, -1, -1):
  # 퇴사일 이후라 일을 못하는 경우
  if consult[i][0] + i > N:
    dp[i] = dp[i+1]
  # 일할 수 있는 경우
  else:
    dp[i] = max(dp[i+1], consult[i][1] + dp[i + consult[i][0]])
print(dp[0]) 
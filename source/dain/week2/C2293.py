n, k = map(int, input().split())
value = [int(input()) for _ in range(n)]
value.sort()
dp = [0] * (k+1)
for i in range(1, k+1):
  arr = []
  for v in value:
    if v <= i and dp[i-v] != -1:
      arr.append(dp[i-v])
    if not arr:
      dp[i] = -1
    else:
      dp[i] = min(arr) + 1
print(dp[k])

# idx = 0
# dp[value[0]] = 1

# for i in range(value[0]+1, k+1):
#   if value[idx] != value[len(value)-1]:
#     if i == value(idx+1):
#       idx += 1
#       dp[i] = 1
#       continue
    
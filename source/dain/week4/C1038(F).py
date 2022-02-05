from collections import defaultdict
n = int(input())
dp = defaultdict(int)
# 숫자로 비교해야 할지 문자로 비교해야 할지
# 문자열로 비교하는 게 맞을 것 같긴 함
while True:
  cnt = i = 1
  if i <= 10:
    dp[i] = i
    i += 1
  cnt += 1
  if i == n:
    break
  if cnt > 9876543210:
    cnt = 1
    break
print(dp[n] if not dp[n] else -1)
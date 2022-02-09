import sys
n, s = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
left = 0
dp = 1e9
# 매번 합을 구해주는 것보다 합을 미리 구해놓는 게 현명한 방법이다
sum_list = [0] * (n+1)
for i in range(1, n+1):
  sum_list[i] = sum_list[i-1] + num[i-1]

for i in range(n+1):
  while (sum_list[i] - sum_list[left]) >= s:
    if (sum_list[i] - sum_list[left+1]) < s:
      break
    left += 1
  if (sum_list[i] - sum_list[left]) >= s:
    dp = min(dp, i-left)
    if dp == 1: break
print(dp) if dp != 1e9 else print(0)
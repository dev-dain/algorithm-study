# 백준 1806 부분합
# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
nums = list(map(int, input().split()))
l, r = 0, 1 # 투 포인터
ans = 1e9 # 최소 길이
sum_n = [0] * (n+1) # 부분합 리스트

for i in range(1, n+1):
    sum_n[i] = sum_n[i-1] + nums[i-1]

while l < n+1 and r < n+1:
    result = sum_n[r] - sum_n[l] # l부터 r까지의 합

    if result >= s: # 합이 s이상이면 최소길이를 갱신 왼쪽 포인터 이동
        ans = min(ans, r-l)
        l += 1
    else: # 합이 s미만이면 오른쪽 포인터 이동
        r += 1

print(0) if ans == 1e9 else print(ans)
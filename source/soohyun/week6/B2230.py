# 백준 2230 수 고르기
# https://www.acmicpc.net/problem/2230

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

l, r = 0, 1
ans = a[n-1] - a[0]

while l < n and r < n:
    diff = a[r] - a[l] # 수의 차이

    if diff < m:
        r += 1
    else:
        ans = min(ans, diff)
        if diff == m: break
        l += 1

print(ans)
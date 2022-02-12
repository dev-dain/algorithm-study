import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input().strip())

a = sorted(a)
ans = sys.maxsize
# 투포인터
left, right = 0, 1
while left < n and right < n:
    tmp = a[right] - a[left]
    if tmp == m:
        print(m)
        exit(0)
    if tmp < m:
        right += 1
        continue
    left += 1
    ans = min(tmp, ans)
print(ans)

ans = 4
n, m, h = map(int, input().split())
a = [[0]*n for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1

def ladder():
    for i in range(n):
        k = i
        for j in range(h):
            if a[j][k]:
                k += 1
            elif k > 0 and a[j][k-1]:
                k -= 1
        if i != k:
            return False
    return True

def solve(cnt, x, y):
    global ans
    if ans <= cnt:
        return
    if ladder():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if a[i][j]:
                j += 1
            else:
                a[i][j] = 1
                solve(cnt+1, i, j+2)
                a[i][j] = 0

solve(0, 0, 0)
print(ans if ans < 4 else -1)
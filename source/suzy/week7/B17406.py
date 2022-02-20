from itertools import permutations
from copy import deepcopy
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rcs = [list(map(int, input().split())) for _ in range(k)]

ans = float('inf')

# 회전 순서
for p in permutations(rcs, k):
    # 원본 복사
    cp_a = deepcopy(a)
    for r,c,s in p:
        r -= 1
        c -= 1
        for n in range(s,0,-1):
            tmp = cp_a[r-n][c+n]
            cp_a[r-n][c-n+1:c+n+1] = cp_a[r-n][c-n:c+n]  # 맨 위쪽
            
            for row in range(r-n, r+n): # 왼쪽 테두리
                cp_a[row][c-n] = cp_a[row+1][c-n]
                
            cp_a[r+n][c-n:c+n] = cp_a[r+n][c-n+1:c+n+1] # 맨 아리쪽
            
            for row in range(r+n, r-n,-1): # 오른쪽 테두리
                cp_a[row][c+n] = cp_a[row-1][c+n]
                
            cp_a[r-n+1][c+n] = tmp
            
    # 각 행의 최소값
    for row in cp_a:
        ans = min(ans, sum(row))
print(ans)
            
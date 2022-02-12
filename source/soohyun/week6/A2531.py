# 백준 2531 회전 초밥
# https://www.acmicpc.net/problem/2531

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
l = 0
ans = 0 # 초밥 가짓수의 최대값

while l < n:
    eat = set() # 먹는 초밥 종류
    r = l + k
    flag = True # 쿠폰을 사용할 수 있는지 체크

    for i in range(l, r):
        i %= n
        eat.add(sushi[i])
        if sushi[i] == c: flag = False

    cnt = len(eat)
    if flag: cnt += 1
    ans = max(ans, cnt)
    
    l += 1

print(ans)
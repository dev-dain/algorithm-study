# 백준 15961 회전 초밥
# https://www.acmicpc.net/problem/15961

from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
l, r = 0, 0
eat = defaultdict(int)
eat[c] += 1 # 쿠폰은 미리 센다
ans = 0 # 먹을 수 있는 가짓수의 최대값

while l < n:
    eat[sushi[r % n]] += 1 # 오른쪽 스시 추가

    # 슬라이딩 윈도우
    if r >= k-1:
        ans = max(ans, len(eat))
        
        eat[sushi[l % n]] -= 1 # 왼쪽 스시 삭제
        if eat[sushi[l % n]] == 0: # 0개라면 딕셔너리에서 제거
            del eat[sushi[l % n]]
        
        l += 1
    
    r += 1

print(ans)
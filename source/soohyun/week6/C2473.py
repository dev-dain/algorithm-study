# 백준 2473 세 용액
# https://www.acmicpc.net/problem/2473

import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))
sol.sort() # 오름차순 정렬

result = sys.maxsize # 세 용액의 합
ans = [0, 0, 0] # 세 용액

for i in range(n-2):
    l, r = i+1, n-1

    while l < r:
        mix = sol[i] + sol[l] + sol[r] # 새로운 세 용액의 합

        if abs(mix) < abs(result): # 기존의 세 용액의 합보다 작다면 갱신
            result = mix
            ans = [sol[i], sol[l], sol[r]]

        if mix == 0:
            break
        elif mix < 0:
            l += 1
        else:
            r -= 1

print(*ans)
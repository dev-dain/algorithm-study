# 백준 15686 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
house, chicken = [], [] # 집과 치킨집 위치
answer = 1e9 # 치킨거리 최소값

# 집과 치킨집 위치 구하기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

coms = list(combinations(chicken, M)) # M개의 치킨집 조합

for com in coms:
    dist = [1e9] * len(house) # 각 집의 치킨거리
    for cx, cy in com:
        for i in range(len(house)):
            dist[i] = min(dist[i], abs(cx - house[i][0]) + abs(cy - house[i][1]))
    answer = min(answer, sum(dist))

print(answer)
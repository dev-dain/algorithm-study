# 백준 11265 끝나지 않는 파티
# https://www.acmicpc.net/problem/11265

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 모든 파티장에서 모든 파티장까지 최단거리 구하기
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(M):
    A, B, C = map(int, input().split())

    if graph[A-1][B-1] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')
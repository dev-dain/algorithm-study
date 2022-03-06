# 백준 1967 트리의 지름
# https://www.acmicpc.net/problem/1967

import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(node, result):
    for x, c in graph[node]:
        if cost[x] == -1: # 아직 방문하지 않는 경우 가중치 합을 구한다
            cost[x] = result + c
            dfs(x, result + c)

# 1번 노드를 기준으로 가중치 합 구하기
cost = [-1] * (n+1)
cost[1] = 0
dfs(1, 0)

start = cost.index(max(cost)) # 1번 노드에서 가장 먼 노드
# 가장 먼 노드를 기준으로 가중치 합 구하기
cost = [-1] * (n+1)
cost[start] = 0
dfs(start, 0)

print(max(cost)) # 트리의 지름
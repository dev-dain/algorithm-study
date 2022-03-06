# 벡준 13023 ABCDE
# https://www.acmicpc.net/problem/13023

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, idx):
    if idx == 4: # 친구 관계가 존재한다면 결과 출력 후 종료
        print(1)
        exit(0)

    # 친구 관계 탐색
    for i in graph[node]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, idx+1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(0) # 친구 관계가 존재하지 않는 경우
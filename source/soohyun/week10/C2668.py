# 벡준 2668 숫자고르기
# https://www.acmicpc.net/problem/2668

n = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
ans = []

# 숫자 연결관계 구하기
for i in range(n):
    num = int(input())
    graph[num].append(i+1)

def dfs(node):
    for j in graph[node]:
        if visited[j]:
            ans.append(j)
        else: # 사이클이 존재하면 조건에 해당하는 집합이다
            visited[j] = 1
            dfs(j)
            visited[j] = 0

# 1부터 n까지 모든 숫자 탐색
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = 1
        dfs(i)
        visited[i] = 0

print(len(ans))
for a in ans: print(a)
# 백준 1504 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

import heapq, sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist = [1e9] * (N+1) # 최단거리 리스트
    dist[start] = 0

    while queue:
        cur_dist, cur_node = heapq.heappop(queue) # 가장 거리가 짧은 노드
        if dist[cur_node] < cur_dist: # 최단거리가 현재 노드거리보다 작다면 넘어간다
            continue
        for next_node, next_dist in graph[cur_node]: # 현재 노드와 연결된 인접 노드 확인
            cost = cur_dist + next_dist
            if cost < dist[next_node]: # 현재 노드를 거쳐서 가는 거리가 다음 노드거리보다 작다면 최단거리 갱신
                heapq.heappush(queue, (cost, next_node))
                dist[next_node] = cost

    return dist

dist_start = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# start -> v1 -> v2 -> end 와 start -> v2 -> v1 -> end 중 더 짧은 거리 구하기
answer = min(dist_start[v1] + dist_v1[v2] + dist_v2[N], dist_start[v2] + dist_v2[v1] + dist_v1[N])
print(-1) if answer >= 1e9 else print(answer) # 최단경로 유무에 따른 결과 출력
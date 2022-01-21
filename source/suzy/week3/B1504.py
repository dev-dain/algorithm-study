import heapq
import sys
input = sys.stdin.readline

INF = float('inf')

# 노드 N 간선 E
N, E = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    road[a].append([c,b])
    road[b].append([c,a])

# 반드시 거쳐야하는 두 정점
v1, v2 = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * (N+1)
    dist[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])
  
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for c, n in road[node]:
            if dist[n] > dist[node] + c:
                dist[n] = dist[node] + c
                heapq.heappush(heap, [dist[n], n])
    return dist[end]

# 1 (2-3) 4
path1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N)
# 1 (3-2) 4
path2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N)

result = min(path1, path2)
print(result if result < INF else -1)
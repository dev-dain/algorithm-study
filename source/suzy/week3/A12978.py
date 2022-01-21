import heapq

def dijkstra(dist,adj):
    # 출발노드를 기준으로 각 노드들의 최소비용 탐색
    heap = []
    heapq.heappush(heap, [0,1])  # 거리,노드
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in adj[node]:
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [cost+c,n])


def solution(N, road, K):
    dist = [float('inf')]*(N+1)  # dist 배열 만들고 최소거리 갱신할거임
    dist[1] = 0  # 1번은 자기자신이니까 거리 0
    adj = [[] for _ in range(N+1)]  # 인접노드&거리 기록할 배열
    for r in road: # adj 각 노드에 연결된 노드 - 거리로 저장
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dist,adj)
    
    return len([i for i in dist if i <=K])
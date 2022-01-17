# 프로그래머스 12978 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def dijkstra(start, graph, dist):
    queue = []
    # 시작노드는 큐에 삽입하고, 최단경로는 0
    heapq.heappush(queue, [0, start])
    dist[start] = 0
    
    while queue:
        now_dist, now_node = heapq.heappop(queue) # 가장 거리가 짧은 노드
        if dist[now_node] < now_dist: # 최단거리가 현재 노드거리보다 작다면 넘어간다
            continue
        for next_node, next_dist in graph[now_node]: # 현재 노드와 연결된 인접 노드 확인
            cost = now_dist + next_dist
            if cost < dist[next_node]: # 현재 노드를 거쳐서 가는 거리가 다음 노드거리보다 작다면 최단거리 갱신
                dist[next_node] = cost
                heapq.heappush(queue, [cost, next_node])

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    dist = [1e9] * (N+1)
    
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    dijkstra(1, graph, dist)
    answer = len([d for d in dist if d <= K]) # K시간 이하로 배달이 가능한 마을 수
    
    return answer
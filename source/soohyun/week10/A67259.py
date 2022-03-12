# 프로그래머스 67259 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    n = len(board)
    cost = [[[1e9] * n for _ in range(n)] for _ in range(4)] # 방향, 위치에 따른 비용 리스트
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동남서북
    queue = deque([])
    
    # 시작점 초기화
    for i in range(4):
        cost[i][0][0] = 0
        
    # 0행 1열 초기화
    if board[0][1] == 0:
        queue.append([0, 1, 0, 100])
        cost[0][0][1] = 100
    
    # 1행 0열 초기화
    if board[1][0] == 0:
        queue.append([1, 0, 1, 100])
        cost[1][1][0] = 100
    
    while queue:
        x, y, d, c = queue.popleft() # 위치, 방향, 비용
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]: # 이동 가능한 범위이며 빈칸인 경우
                new_cost = c + 100 if d == i else c + 600 # 다음 위치의 비용
                if cost[i][nx][ny] > new_cost: # 기존 다음 위치 비용보다 더 작다면 비용 갱신
                    cost[i][nx][ny] = new_cost
                    queue.append([nx, ny, i, new_cost])   
    
    return min([cost[i][-1][-1] for i in range(4)]) # 최소 비용
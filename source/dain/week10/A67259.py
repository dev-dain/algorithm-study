from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(board):
    answer = 1e9
    N = len(board)
    tmp_board = [[1e9 for _ in range(N)] for _ in range(N)]

    qu = deque()
    qu.append((0, 0, 1, 0))
    qu.append((0, 0, 2, 0))

    while qu:
        x, y, dir, tmp_cost = qu.popleft()
        
        if x == N-1 and y == N-1:
            answer = min(answer, tmp_cost)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cost = 0
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
                continue
            if dir+2 == i or dir-2 == i:
                continue
            if dir == i:
                cost = 100
            else:
                cost = 500 + 100
            if tmp_board[nx][ny] >= tmp_cost + cost:
                tmp_board[nx][ny] = tmp_cost + cost
                qu.append((nx, ny, i, tmp_cost + cost))
            
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
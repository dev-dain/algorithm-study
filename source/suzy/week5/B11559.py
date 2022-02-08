from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    for d in range(4):	# 상하좌우
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < 12 and 0 <= Y < 6:
            # 같은 색깔인 경우
            if board[X][Y] == board[x][y] and visited[X][Y] == 0:
                q.append([X, Y])
                visited[X][Y] = 1

def down():
    for y in range(6):
        tmp = deque([])
        for x in range(11, -1, -1):
            # 뿌요 위치 저장
            if board[x][y] != '.':
                tmp.append(board[x][y])
        for x in range(11, -1, -1):
            if tmp:	# 뿌요를 하나씩 꺼내어 보드에 기록
                board[x][y] = tmp.popleft()
            else:	# 비면 뿌요 없음
                board[x][y] = '.'

board = [list(input()) for _ in range(12)]

chk = 0
answer = 0
while True:		# 새로 터지는 뿌요가 없을 때까지 반복
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([[i, j]])
                # print(q)             
                stack = []	# 뿌요 위치를 기록할 스택
                while q:
                    x,y = q.popleft()
                    print(q)
                    stack.append([x,y])
                    bfs(x, y)
                if len(stack) >= 4:	# 이어진 뿌요가 4개 이상일 때
                    chk = 1
                    for s in stack:
                        board[s[0]][s[1]] = '.'	# 뿌요 터진경우
    down()
    if chk == 0:
        break
    chk = 0
    answer += 1
print(answer)
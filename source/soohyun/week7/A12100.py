# 백준 12100 2048(Easy)
# https://www.acmicpc.net/problem/12100

from collections import deque
import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans, q = 0, deque() # 블록 최대값

def solve(count):
    global ans, board

    if count == 5: # 이동횟수 = 5인 경우 최대값을 구하고 멈춘다
        for b in board:
            ans = max(ans, max(b))
        return

    tmp = copy.deepcopy(board) # 원본 board 저장

    for i in range(4):
        move(i)
        solve(count+1)
        board = copy.deepcopy(tmp)

# 이동할 수 있는 블록 구하기
def get(x, y):
    if board[x][y]:
        q.append(board[x][y])
        board[x][y] = 0

# 블록 합치기
def merge(x, y, dx, dy):
    while q:
        v = q.popleft()
        if board[x][y] == 0: # 앞의 숫자가 0이면 빈칸이므로 현재 숫자를 앞의 숫자에 옮긴다
            board[x][y] = v
        elif board[x][y] == v: # 앞의 숫자와 현재 숫자가 같다면 앞의 숫자를 2배해준다
            board[x][y] = v * 2
            x, y = x + dx, y + dy
        else: # 앞의 숫자와 현재 숫자가 다르다면 인덱스를 이동한 후 현재 숫자를 옮긴다
            x, y = x + dx, y + dy
            board[x][y] = v

# 블록 이동하기
def move(d):
    if d == 0: # 상
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif d == 1: # 하
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0)
    elif d == 2: # 좌
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else: # 우
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1)

solve(0)
print(ans)
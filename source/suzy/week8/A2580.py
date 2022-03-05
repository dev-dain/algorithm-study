import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
# 빈칸 좌표 저장
blank = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

# 행에 들어갈 수 있는지
def checkrow(x, k):
    for i in range(9):
        if sudoku[x][i] == k: # 이미 존재하는 경우
            return False
    return True
# 열에 들어갈 수 있는지
def checkcol(y, k):
    for i in range(9):
        if sudoku[i][y] == k:
            return False
    return True
# 정사각형에 들어갈 수 있는지
def checkrect(x, y, k):
    nx = x // 3*3
    ny = y // 3*3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == k:
                return False
    return True

# 재귀함수의 깊이 idx
def dfs(idx):
    if idx == len(blank):
        for row in sudoku: print(*row)
        exit(0)
        
    x, y = blank[idx]
    for num in range(1, 10):
        # 빈칸에 넣을 수 있는 숫자인 경우 다음 빈칸
        if checkrow(x, num) and checkcol(y, num) and checkrect(x, y, num):
            sudoku[x][y] = num
            dfs(idx+1)
            sudoku[x][y] = 0 # 초기화
dfs(0)
# 백준 2580 스도쿠
# https://www.acmicpc.net/problem/2580

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0] # 스도쿠의 빈칸 리스트

# 행에 들어갈 수 있는지 체크
def check_row(x, k):
	for i in range(9):
		if sudoku[x][i] == k:
			return False
	return True

# 열에 들어갈 수 있는지 체크
def check_col(y, k):
	for i in range(9):
		if sudoku[i][y] == k:
			return False
	return True

# 정사각형에 들어갈 수 있는지 체크
def check_rect(x, y, k):
	nx = x // 3 * 3
	ny = y // 3 * 3

	for i in range(3):
		for j in range(3):
			if sudoku[nx+i][ny+j] == k:
				return False
	return True

def dfs(idx):
	# 빈칸을 다 채웠다면 출력하고 종료
	if idx == len(blank):
		for row in sudoku: print(*row)
		exit(0)
	
	x, y = blank[idx] # 빈칸의 위치
	for num in range(1, 10):
		# 빈칸에 넣을 수 있는 숫자인 경우 다음 빈칸으로 넘어간다
		if check_row(x, num) and check_col(y, num) and check_rect(x, y, num):
			sudoku[x][y] = num
			dfs(idx + 1)
			sudoku[x][y] = 0 # 초기화

dfs(0)
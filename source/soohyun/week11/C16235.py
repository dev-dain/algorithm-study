# 백준 16235 나무 재테크
# https://www.acmicpc.net/problem/16235

from collections import deque

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)] # 위치별 나무 리스트
nour = [[5] * n for _ in range(n)] # 위치별 양불 리스트
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1] # 동, 동남, 남, 남서, 서, 서북, 북, 북동

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

def spring_summer():
    for x in range(n):
        for y in range(n):
            l = len(tree[x][y])
            for i in range(l):
                # 봄 - 양분이 충분한 경우 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다
                if tree[x][y][i] <= nour[x][y]:
                    nour[x][y] -= tree[x][y][i]
                    tree[x][y][i] += 1
                # 여름 - 양분이 부족한 경우 나무가 죽고, 죽은 나무가 양분으로 변한다
                else:
                    for _ in range(i, l):
                        nour[x][y] += tree[x][y].pop() // 2
                    break

def fall_winter():
    for x in range(n):
        for y in range(n):
            # 가을 - 나무의 나이가 5의 배수인 경우 인접한 칸에 나이가 1인 나무가 생긴다
            for t in tree[x][y]:
                if t % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)
            # 겨울 - 땅에 양분이 추가된다
            nour[x][y] += a[x][y]

for _ in range(k):
    spring_summer()
    fall_winter()

ans = 0 # 살아있는 나무의 개수
for x in range(n):
    for y in range(n):
        ans += len(tree[x][y])
print(ans)
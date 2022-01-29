r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치
cleaner = []
for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            cleaner.append((i, j))

# 미세먼지 확산
def diffusion():
    global room, cleaner
    temp = [[0]*c for _ in range(r)]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(r):
        for j in range(c):
            if room[i][j]==0 or room[i][j]==-1: continue
            cnt = 0
            for x, y in move:
                cx = i+x
                cy = j+y
                if 0<=cx<r and 0<=cy<c and room[cx][cy]!= -1:
                    temp[cx][cy] += room[i][j]//5
                    cnt += 1
            temp[i][j] += room[i][j]-cnt*(room[i][j]//5)
    temp[cleaner[0][0]][cleaner[0][1]] = -1
    temp[cleaner[1][0]][cleaner[1][1]] = -1
    room = temp

# 공기청정기 작동
def clean(x, y, move):
    last = 0
    j = 0
    start = (x, y)
    x += move[0][0]
    y += move[0][1]
    while x != start[0] or y != start[1]:
        next = room[x][y]
        room[x][y] = last
        last = next
        x += move[j][0]
        y += move[j][1]
        if not (0<=x<r and 0<=y<c):
            if j == 3: break
            x = x - move[j][0] + move[j+1][0]
            y = y - move[j][1] + move[j+1][1]
            j += 1

for _ in range(t):
    diffusion()
    clean(cleaner[0][0], cleaner[0][1], [(0, 1), (-1, 0), (0, -1), (1, 0)])
    clean(cleaner[1][0], cleaner[1][1], [(0, 1), (1, 0), (0, -1), (-1, 0)])
answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j] and room[i][j] != -1:
            answer+= room[i][j]
print(answer)
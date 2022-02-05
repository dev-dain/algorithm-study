N, M, K = map(int, input().split())
board = [[[] for _ in range(N+1)] for _ in range(N+1)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
fireball = []
for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  fireball.append([r, c, m, s, d])
for _ in range(K):
  for i in range(len(fireball)):
    r, c, m, s, d = fireball[i]
    nx, ny = r, c
    for _ in range(s):
      nx = nx + dx[d]
      ny = ny + dy[d]
      if nx < 1:
        nx = N
      elif nx > N:
        nx = 1
      if ny < 1:
        ny = N
      elif ny > N:
        ny = 1
    board[nx][ny].append([m, s, d])
  fireball = []

  for i in range(1, N+1):
    for j in range(1, N+1):
      if not len(board[i][j]):
        continue
      if len(board[i][j]) == 1:
        # fireball.append([i, j] + board[i][j])
        fireball.append([i, j] + board[i][j].pop())
        continue
      mass = 0
      speed = 0
      direct = board[i][j][0][2] % 2
      flag = True
      for m, s, d in board[i][j]:
        mass += m
        speed += s
        if not flag:
          continue
        if d % 2 != direct:
          flag = False
      s_m = mass // 5
      s_s = speed // len(board[i][j])
      board[i][j] = []

      if s_m == 0:
        continue
      for x in range(4):
        # nx = (i + dx[x*2])
        # ny = (j + dy[x*2])
        # if nx < 1:
        #   nx = N
        # elif nx > N:
        #   nx = 1
        # if ny < 1:
        #   ny = N
        # elif ny > N:
        #   ny = 1
        s_d = (x * 2)
        if not flag:
          s_d += 1
        # 왜 nx, ny가 아니라 i, j지? 이해가 안된다
        # 아....!!! 바로 움직이는 게 아니라 분산은 나중에 시키는거구나..
        # 미쳤군.. 이게 문맹이지..
        fireball.append([i, j, s_m, s_s, s_d])
print(sum([ball[2] for ball in fireball]))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution():
  dp = 1  # 최대값
  # x, y, visited
  qu = set([(0, 0, board[0][0])])
  
  while qu:
    # 가능한 경우들을 시도해보되 백트랙킹하기
    # set에서 pop하면 임의의 요소가 나옴
    x, y, visited = qu.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= r or ny >= c:
        continue
      # 다음에 볼 것이 아직 알파벳 모음에 없다면
      if board[nx][ny] not in visited:
        next = visited + board[nx][ny]  # 다음 알파벳 추가
        qu.add((nx, ny, next))  # 큐로 이동
        dp = max(dp, len(next)) # 어떤 것이 더 큰지 비교해 최대값 넣기
  return dp

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
print(solution())
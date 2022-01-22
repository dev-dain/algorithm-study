def solution(n, results):
  score = [[None for _ in range(n)] for _ in range(n)]
  # 승패를 True/False로 지정
  for a, b in results:
    score[a-1][b-1] = True
    score[b-1][a-1] = False

  for i in range(n):
    for j in range(n):
      for k in range(n):
        # 만약 j-i 사이 경기 정보가 없다면 패스
        if not score[j][i]:
          continue
        
        # 만약 j가 i를 이겼고, i가 k를 이겼다면 j가 k를 이긴 것
        # 반대의 경우도 마찬가지임
        if score[j][i] == score[i][k]:
          score[j][k] = score[i][k]
          score[k][j] = not score[i][k]

  res = 0
  for x in range(n):
    # 만약 승부 결정이 나지 않은 짝이 있다면
    # 순위를 알 수 없으므로 넘김
    if None in score[x][:x] + score[x][x+1:]:
      continue
    res += 1
  
  return res

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
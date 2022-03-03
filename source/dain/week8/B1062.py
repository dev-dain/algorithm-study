from itertools import combinations

N, K = map(int, input().split())
learn = [0 for _ in range(N)]
must = ['a', 'n', 't', 'i', 'c']
for i in range(N):
  word = list(input())[4:-4]
  for c in word:
    learn[i] |= (1 << ord(c) - ord('a'))

if K < 5:
  print(0)
  exit(0)
elif K == 26:
  print(N)
  exit(0)

alpha = 'bdefghjklmopqrsuvwxyz'
combi = list(combinations(list(alpha), K-5))
res = 0
for com in combi:
  bit = 0
  for c in must:
    bit |= (1 << ord(c) - ord('a'))
  for c in com:
    bit |= (1 << ord(c) - ord('a'))
    
  cnt = 0
  for i in range(len(learn)):
    if learn[i] & bit == learn[i]:
      cnt += 1
  res = max(res, cnt)
print(res)
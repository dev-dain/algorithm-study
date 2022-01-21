n = int(input())
cnt = 0 
for i in range(n):
  m = input()
  for j in range(0, len(m)-1):
    if m[j] == m[j+1]:
      continue
    elif m[j] in m[j+1:]:
      cnt += 1
      break

print(n-cnt)
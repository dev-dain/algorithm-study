import sys
input = sys.stdin.readline

n = int(input())
input()
s = input()
target = 'IOI' + 'OI' * (n-1)
idx, cnt = 0, 0

while True:
  idx = s.find(target, idx)
  if idx == -1:
    break
  cnt += 1
  idx += 2

# for i in range(len(s)-(2*n)):
#   l, r = i+1, i+2
#   if s[i] == 'I':
#     flag = 0
#     for _ in range(n):
#       if s[l] == 'O' and s[r] == 'I':
#         l += 2
#         r += 2
#       else:
#         break
#     else:
#       flag = 1
#       cnt += 1
print(cnt)
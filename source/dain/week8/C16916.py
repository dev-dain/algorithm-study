from collections import defaultdict
import sys
input = sys.stdin.readline

s = input().rstrip()
alpha_dict = defaultdict(list)
for i in range(len(s)):
  c = s[i]
  alpha_dict[c].append(i)
p = input().rstrip()
loop = True
flag = 0
# idx = 0
while loop:
  # ch = p[idx]
  ch = p[0]
  if not alpha_dict[ch]:
    loop = False
    break
  for idx in alpha_dict[ch]:
    if len(p) + idx > len(s):
      loop = False
      break
    if p == s[idx:idx+len(p)]:
      flag = 1
      loop = False
      break
    
# for i in range(len(s)):
#   if p[0] == s[i] and len(s) - i >= len(p):
#     if p == s[i:i+len(p)]:
#     # if p == ''.join(s[i:i+len(p)]):
#       flag = 1
#       break
  
print(flag)
s = input()
z = o = 0
flag = s[0]
cnt = 0
for i in range(1, len(s)):
  if s[i] != flag:
    if s[i] == '0':
      if not cnt:
        o += 1
        cnt += 1
      z += 1
      flag = '0'
    else:
      if not cnt:
        z += 1
        cnt += 1
      o += 1
      flag = '1'
print(min(z, o))
def solution(n):
  b = list(bin(n)[2:])
  cnt = b.count('1')
  res = n
  while True:
    res += 1
    if bin(res)[2:].count('1') == cnt:
      return res

print(solution(78))
print(solution(15))
print(solution(8))
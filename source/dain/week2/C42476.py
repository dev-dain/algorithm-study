def solution(numbers):
  num = list(map(str, numbers))
  num.sort(key=lambda x: x * 3, reverse=True)
  return str(int(''.join(num)))

# def solution(numbers):
#     if all([True if x == 0 else False for x in numbers]): 
#       return '0'
#     strs = sorted([str(n)[::-1] for n in numbers], reverse=True)
#     return ''.join([s[::-1] for s in strs])  
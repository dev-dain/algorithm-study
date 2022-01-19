def solution(numbers, hand):
  key_dict = {
    1: (0, 0), 2: (0, 1), 3: (0, 2), 
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
  }
  l_idx = key_dict['*']
  r_idx = key_dict['#']
  answer = []

  for n in numbers:
    if n in (1, 4, 7, '*'):
      answer.append('L')
      l_idx = key_dict[n]
    elif n in (3, 6, 9, '#'):
      answer.append('R')
      r_idx = key_dict[n]
    else:
      l_dist = sum([abs(x - y) for (x, y) in zip(key_dict[n], l_idx)])
      r_dist = sum([abs(x - y) for (x, y) in zip(key_dict[n], r_idx)])

      if l_dist < r_dist:
        l_idx = key_dict[n]
        answer.append('L')
      elif l_dist > r_dist:
        r_idx = key_dict[n]
        answer.append('R')
      else:
        if hand == 'left':
          answer.append('L')
          l_idx = key_dict[n]
        else: 
          answer.append('R')
          r_idx = key_dict[n]
    
  return ''.join(answer)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))

# 정렬해서 풀기
def solution(phone_book):
  res = True
  phone_book.sort()
  for i in range(len(phone_book) - 1):
    if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
      return False
  return res

# 해시
def solution(phone_book):
  res = True
  num_dict = {}
  for number in phone_book:
    num_dict[number] = number
  for number in phone_book:
    tmp = ''
    for string in number:
      tmp += string
      if tmp in num_dict and tmp != number:
        return False
  return res

# 내 풀이.. 나 뭐한거묘
def solution(phone_book):
  res = True
  len_list = list(set([len(num) for num in phone_book]))
  len_list.sort()
  num_dict = {}
  for length in len_list:
    for num in phone_book:
      if len(num) == length:
        num_dict[num] = num
        continue
      if num_dict.get(num[:length]):
        if num_dict.get(num[:length]) == num:
          res = 'NO'
        break
      num_dict[num] = num[:length]
    if not res:
      break
  return res

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"]	)
## 1주 문제 1
* 🥈❓ [백준 2504 괄호의 값](https://www.acmicpc.net/problem/2504)

* 접근 방법
	* 입력을 고려했을 때 sys.stdin.readline을 쓰지 않고 그냥 input을 써도 될 것 같은 문제
	* 괄호 문제는 대부분 *스택*으로 푸는 문제
		* 그래서 자료구조 문제로 접근하고 풀이 방법을 생각
	* 단, 다른 괄호 문제와 달리 소괄호와 대괄호가 섞여 있고 곱셈, 덧셈 연산을 해야 해서 어려운 문제
	* 규칙 1 : 여는 괄호 (, [라면 스택에 push
	* 규칙 2 : 닫는 괄호 )일 때, 스택의 top에 있는 것이 [이거나 스택이 비었다면 에러. 바로 중단. 마찬가지로 닫는 괄호 ]일 때, 스택의 top에 있는 것이 (이거나 스택이 비었다면 에러이므로 바로 중단.
	* 여기까지는 생각했지만, 값을 어디에 저장하고 계산해야 할지가 난관이었음
	* 그래서 20분 정도 고민하다가 결국 블로그에 풀이를 찾아봄  
  
* 정리된 풀이
	* 여는 괄호를 스택에 넣을 때, 그냥 push만 할 것이 아니라 **해당 괄호에 해당하는 값을 temp에 곱한다.** 
		* temp의 초기값은 1이어야 함 (곱해야 하니까)
		* 이 방법은 처음 봤을 때 이해하기는 어렵지만 신선함
	* 닫는 괄호가 나올 때, **지금 검사하는 것의 이전 인덱스의 괄호가 짝이 맞아서 쌍을 이루는 괄호라면 temp를 최종 결과인 result에 더함. (괄호가 계산된 것이기 때문에)**
	* 그 후 temp를 해당 괄호에 해당하는 값으로 나눈 뒤, 괄호를 계산한 셈이므로 pop함
	* 최종적으로, res가 답이 됨
	* 또 하나, for문을 돌릴 때 for-in이 아니라 전체 입력 s의 길이만큼 range 객체를 만들어야 함. 그래야 이전 위치의 괄호와 현재 괄호를 비교할 수 있음

---
* 정답 코드
```python
s = input()
stack = []
tmp = 1
res = 0

# for c in s를 하면 안 되고 길이로 돌아야 함
for i in range(len(s)):
  if s[i] == '(':
    tmp *= 2
    stack.append(s[i])
  elif s[i] == '[':
    tmp *= 3
    stack.append(s[i])

  elif s[i] == ')':
    if not stack or stack[-1] == '[':
      res = 0
      break
    if s[i-1] == '(':
      res += tmp
    tmp //= 2
    stack.pop() # pop도 까먹지 말고 꼭
  
  else:
    if not stack or stack[-1] == '(':
      res = 0
      break
    # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
    # 단, 이 경우는 오류는 아님
    if s[i-1] == '[':
      res += tmp
    tmp //= 3
    stack.pop() # pop 까먹지 말기

if stack:
  res = 0
print(res)
```
- 시간복잡도 : O(n)
- 공간복잡도 : O(n)
- 문제 유형 : 스택, 문자열, 구현
---
---
## 1주 문제 2
* 1️⃣[프로그래머스 77484 로또의 최고 순위와 최저 순위](https://programmers.co.kr/learn/courses/30/lessons/77484) 
* 접근 방법
	* 평범하고 무난한 구현 문제. 파이썬에서는 set 자료형을 쓰면 쉽게 풀 수 있음
	* 일단 입력으로 들어오는 lottos와 win_nums를 교집합 연산(&)으로 계산해 일치하는 숫자의 개수(match)를 구함
	* 그런 다음 0의 개수를 세고, 0이 없다면 숫자의 개수에 해당하는 등수를 보내줌
		* 등수 매기기는 num = [6, 6, 5, 4, 3, 2, 1] 리스트를 이용하기로 함
	* 0이 있다면, match가 최저이며, match+0의 개수가 최고 등수임
	* 최고/최악의 경우를 고려하는 것이기 때문에 값을 직접 대입할 필요 없음
---
* 정답 코드
```python
def solution(lottos, win_nums):
  lotto = set(sorted(lottos))
  win_num = set(sorted(win_nums))
  match = len(lotto & win_num)
  num = [6, 6, 5, 4, 3, 2, 1]

  if 0 not in lotto:
    return [num[match], num[match]]
  return [num[match + lottos.count(0)], num[match]]
```
- 시간복잡도 : O(1)
- 공간복잡도 : O(n)
- 문제 유형 : 집합, 구현

## 2주 공통 문제 1
* 🥈 [백준 1439 뒤집기](https://www.acmicpc.net/problem/1439)

* 접근 방법
	* 입력을 고려했을 때 sys.stdin.readline을 쓰지 않고 그냥 input을 써도 될 것 같은 문제
	* 연속되어 나타나는 숫자들의 쌍 개수를 어떻게 구해야 할지 고민해야 함
	* 아무리 생각해도 O(N) 이하로는 풀 수 없는 문제
	* 근데.. 이렇게 단순하게 풀어도 되나? 싶은 수준으로 풀었기 때문에 아직도 의구심은 남는 문제
   
* 정리된 풀이
	* 입력을 받고, 0과 1 쌍을 뒤집어야 하는 횟수 z와 o를 따로 만들어 0으로 초기화
  * flag는 입력된 문자열의 맨 처음 숫자를 가리킴
  * cnt는 flag가 처음 변경될 때 딱 1번 셈
  * 문자열 전체를 돌면서, flag와 현재 문자가 다르다면 뒤집어야 하는 쌍이 생기는 것이므로 해당 문자의 카운트를 늘려 주고, flag를 갱신함
  * 적게 뒤집는 횟수를 구하는 문제이므로 min 함수를 사용해 답 구하기 

---
* 정답 코드
```python
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
```
- 시간복잡도 : O(n)
- 공간복잡도 : O(n)
- 문제 유형 : 문자열, 구현
---
---
## 2주 공통 문제 2
* 🥈❓ [백준 5525 IOIOI](https://www.acmicpc.net/problem/5525)
* 접근 방법
	* 서브태스크가 있고 substring들을 세어야 하는 문제기 때문에 좀 까다로워 보였음 (괜히 골랐다 싶었어요 ㅎㅎ)
	* S의 길이는 버리고, 타겟의 IOI 숫자와 전체 문자열만 받으면 됨
	* find 메소드로 전체 문자열에서 타겟을 계속 찾아나가기로 결정
  
* 문제
  * 문제는 50점만 맞은 반쪽짜리 코드라는 것
  * 이 문제에서 만점을 받으려면 보통 방법으로는 안 되고, KMP 알고리즘을 사용하거나 반복문을 1번만 사용해야 한다고 함
  * 문자열을 다루는 심화 알고리즘과 자료구조로는 [KMP 알고리즘](https://blog.encrypted.gg/857), [Trie](https://ko.wikipedia.org/wiki/%ED%8A%B8%EB%9D%BC%EC%9D%B4_(%EC%BB%B4%ED%93%A8%ED%8C%85)), [라빈 카프 알고리즘](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) 등이 있음. 이 중 Trie는 카카오 코딩테스트에 종종 나옴.
  * 결국 반복문 하나만 쓰는 걸 못 한 관계로.. 50점만 맞은 문제. 이해하고 나서 블로그에 정리하기로 함.
---
* 50점 정답 코드 1 (80ms)
```python
n = int(input())
input()
s = input()
target = 'IOI' + 'OI' * (n-1)
idx, cnt = 0, 0

while True:
  idx = s.find(target, idx) # find 사용
  if idx == -1:
    break
  cnt += 1
  idx += 2
print(cnt)
```
  
* 50점 정답 코드 2 (160ms)
```python
import sys
input = sys.stdin.readline

n = int(input())
input()
s = input()
target = 'IOI' + 'OI' * (n-1)
idx, cnt = 0, 0

for i in range(len(s)-(2*n)):
  l, r = i+1, i+2 # 혹시나 하고 for문도 돌려봄
  if s[i] == 'I':
    flag = 0
    for _ in range(n):
      if s[l] == 'O' and s[r] == 'I':
        l += 2
        r += 2
      else:
        break
    else:
      flag = 1
      cnt += 1
print(cnt)
```
- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N)
- 문제 유형 : 문자열, 구현, KMP

## 2주 공통 문제 3
* 🥇❓ [백준 9935 문자열 폭발](https://www.acmicpc.net/problem/9935)
  
* 접근 방법
	* 입력을 고려했을 때 sys.stdin.readline을 쓰지 않고 그냥 input을 써도 될 것 같은 문제
	* 딱 보면 그냥 .replace 계속 하면 되는 문제
	* 골드일 리가 없는데.. 하고 제출했으나 역시나 시간 초과. Pypy3로 제출해도 시간 초과가 나서 언어 문제가 아니라는 생각이 듦
  * 골드 문자열 문제 중 몇 가지는 스택으로 풀어야 된다는 걸 알긴 했는데 문자열의 앞부분부터 스택과 비교해야 하나 생각하다가 결국 검색함
   
* 정리된 풀이
	* 전체 문자열을 순서대로 하나씩 스택에 넣되, 지금 넣는 문자가 터지는 문자열의 맨 "마지막" 문자와 일치한다면, 스택을 역순으로 보면서 터지는 문자열과 같은지 확인
  * 만약 그 부분을 스택에서 싹 지움
  * for문이 끝나면 스택을 문자열로 묶음. 이 때, 문자열에 뭔가 남았다면 그대로 출력하고 아니면 FRULA 출력
  * for문 한 번으로 끝나므로 O(N) 시간 복잡도로 끝날 수 있음
  
---
* 시간초과 코드
```python
s = input()
bomb = input()

while True:
  idx = s.find(bomb)
  if idx == -1:
    break
  s = s.replace(bomb, '') 
  # 아마 이 부분에서 시간초과가 나는 듯함. 
  # 내부적으로 계속 bomb를 찾고 바꾸기 때문에

print(s if s else 'FRULA')
```

* 정답 코드
```python
s = input()
bomb = input()
stack = []

for c in s:
  stack.append(c)
  if c == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
    del stack[-len(bomb):]

print(''.join(stack) if ''.join(stack) else 'FRULA')
```
- 시간복잡도 : O(n)
- 공간복잡도 : O(n)
- 문제 유형 : 문자열, 구현, 스택
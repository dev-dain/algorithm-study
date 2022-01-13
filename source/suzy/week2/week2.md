## 2주차
### 1) [백준 5525] (https://www.acmicpc.net/problem/5525)
- 문제 유형: 문자열
- 시간 복잡도: O(logN)  |  공간 복잡도: O(1)
- 접근 방법
    - IO 가 교대로 반복되는 문자열이다
    - 반복되는 문자열을 찾아 횟수를 세어준다
<br/><br/>
* 풀이
  * 주어진 문자열 index 와 IOI 패턴을 만족하는지 확인한다
  * 연속된 횟수를 세어주고 n과 같을 경우 answer 증가시킨다
<br/><br/>
- 코드
```python
n = int(input())
m = int(input())
s = str(input())

cnt = 0
answer = 0
i = 0 
while i < m-1:
    if s[i-1] == 'I'and s[i]=='O' and s[i+1] == 'I':
        cnt += 1
        if cnt == n:
            cnt -= 1
            answer += 1
        i += 1
    else:
        cnt = 0
    i += 1            
          
print(answer)
```
---

### 2) [백준 1439] (https://www.acmicpc.net/problem/1439)
- 문제 유형: 문자열, 그리디
- 시간 복잡도: O(n) |  공간 복잡도: O(1)
- 접근 방법
    - 첫 시도는 0으로 바꾸는 방법과 1로 바꾸는 방법의 수를 모두 구해서 더 적은 방법을 답으로 출력했다 ( 틀림 ! )
    - 다른 분들의 코드를 보니 0->1 1->0 일 경우만 count 하여 해결했다 .. 
<br/><br/>
* 풀이
  * 입력 받은 문자열의 수만큼 돌며 다를 경우 바꾸어주는 경우이므로 cnt + 1
  * 0 또는 1 둘 중 하나로만 바꾸면 되기 때문에 //2 를 해준다
  * 뒤집어야할 횟수는 변환해야하는 경우에 +1 한 후 2로 나눈 몫이다
<br/><br/>
- 코드
```python
s = str(input())

cnt = 0

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    cnt += 1
print((cnt+1)//2)
```
---

### 3) [백준 9935] (https://www.acmicpc.net/problem/9935)
- 문제 유형: 문자열, 스택
- 시간 복잡도:  O(N+M)  |  공간 복잡도: O(N)
- 접근 방법
    - 문자열에 replace(폭발문자열, '', 1)로 한번에 하나씩 없애서 남은 문자열 길이가 0이라면 FRULA 를 출력하고 아니라면 남은 문자열을 출력했다 ( 시간 초과 )
    - 다른 풀이를 찾아보니 stack을 사용해야하는 문제였다
<br/><br/>
* 풀이
  * 문자열을 차례로 스택에 넣어주고 폭탄의 길이보다 길거나 같다면 뒤에서 부터 비교한다 ( 112ab 12ab 같은 경우)
  * 같다면 stack에서 제거 
  * stack 에 남은 문자열을 출력하거나 비어있다면 FLURA 출력
<br/><br/>
- 코드
```python
import sys
s = list(sys.stdin.readline().rstrip())
e = list(sys.stdin.readline().rstrip())

stack = []

for i in range(len(s)):
    stack.append(s[i])
    if stack[-1] == e[-1] and len(stack) >= len(e):
        if stack[-len(e):] == e:
            for i in range(len(e)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")        

```


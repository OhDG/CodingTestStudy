# Greedy

## 당장 좋은 것만 선택하는 그리디

### 그리디 알고리즘

> 어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘<br>
> 탐욕적 : 현재 상황에서 지금 당장 좋은 것만을 고르는 방법

-   특정한 문제를 만났을 때 단순히 현재 상황에서 가장 좋아보이는 것만을 선택해도 문제를 풀 수 있는지를 파악할 수 있어야 한다.
-   문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다.
-   대체로 이 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있다.

---

### 거스름돈

> 문제
>
> > 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

> 문제 해결
>
> > '가장 큰 화폐 단위부터' 돈을 거슬러 주는 것

```python
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_typess:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
```

> > 화폐의 종류만큼 반복을 수행해야 한다. -> 화폐의 종류가 K개라고 할 때 시간복잡도는 O(K)

---

### 그리디 알고리즘의 정당성

-   탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있을 때는 매우 효과적이고 직관적이다.
-   거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.
-   대부분의 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다.

---

## 큰 수의 법칙

### 저자의 '큰 수의 법칙'
> 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

---

### 큰 수의 법칙 문제
> 문제
>> 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오. <br> <br>
입력 조건
>> - 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다. 
>> - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다. 
>> - 입력으로 주어지는 K는 항상 M보다 작거나 같다. 

>>출력 조건
>> - 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

<br>

> 문제 해설
>> 이 문제를 해결하려면 일단 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다. 연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복하면 된다.
<br>
```python
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수 
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기 
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기 
    if m == 0 : # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)
```
---

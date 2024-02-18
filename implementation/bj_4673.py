# 4673 셀프 넘버
def dr(n):
    result = n + ( n // 10000 ) + ( (n%10000) // 1000 ) + ( (n%1000) // 100 ) + ( (n%100) // 10 ) + ( n % 10 )
    return result

arr = [False for m in range(10001)]

for i in range(10001):
    if dr(i) > 10000:
        continue
    arr[dr(i)] = True

for k in range(1, 10001):
    if arr[k] == False:
        print(k)
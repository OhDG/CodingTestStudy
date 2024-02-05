import sys

n, k = map(int, input().split())

arr = [i for i in range(1, n)]
idx = -1 
total_idx = n-1
print("<", end="")
for m in range(n):
    
    if m == 0:
        idx += k
    else:
        idx += (k-1)

    if idx > total_idx:
        idx -= (total_idx+1)
    
    total_idx -= 1
    print(arr[idx], end="")
    if m == n - 1:
        break
    print(", ", end="")
    arr.pop(idx)

print(">")


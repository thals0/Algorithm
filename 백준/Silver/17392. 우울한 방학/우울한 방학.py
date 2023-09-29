n,m = map(int, input().split())
dep = 0
sum = 0
left = 0

arr = list(map(int, input().split()))
for i in arr:
    sum += i + 1

if sum < m:
    left = m - sum
    div1 = left // (n + 1)
    div2 = left % (n + 1)
    for i in range(1, div1 + 1):
        dep += i ** 2 * (n + 1)
    dep += (div1 + 1) ** 2 * div2

print(dep)
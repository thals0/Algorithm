n = int(input())

isused1 = [0 for _ in range(n)]
isused2 = [0 for _ in range((n-1)*2 + 1)]
isused3 = [0 for _ in range((n-1)*2 + 1)]

cnt = 0

def back(cur):
    global cnt
    if cur == n:
        cnt += 1
        return 
    for i in range(n):
        if isused1[i] or isused2[i+cur] or isused3[cur-i+n-1]:
            continue
        isused1[i] = 1
        isused2[i+cur] = 1
        isused3[cur-i+n-1] = 1
        back(cur+1)
        isused1[i] = 0
        isused2[i+cur] = 0
        isused3[cur-i+n-1] = 0

back(0)
print(cnt)
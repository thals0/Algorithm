from collections import Counter
import sys

a = int(sys.stdin.readline())
b= []
for i in range(a):
  b.append(int(sys.stdin.readline()))

b.sort()

c = a//2 

# 산술평균
print(round(sum(b)/a))
# 중앙값
print(b[c])

# 최빈값
# counts = dict()
# for i in range(1, a+1):
#   counts[i] = []

# maxCount = 1
# count = 1
# for j in range(1,a):
#   if b[j] == b[j-1]:
#     count += 1
#   else:
#     counts[count].append(b[j-1])
#     if maxCount < count : maxCount = count 
#     count = 1
#   if j == a-1:
#     counts[count].append(b[j])
#     if maxCount < count : maxCount = count
# if a ==1:
#   counts[1].append(b[0])

# counts[maxCount].sort()
# if len(counts[maxCount]) == 1:
#   print(counts[maxCount[0]])
# else:
#   print(counts[maxCount][1])

cnt = Counter(b).most_common(2)

if len(b)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
  print(cnt[0][0])



# 최댓값 - 최소값
print(b[a-1]-b[0])

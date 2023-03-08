# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#   n = int(input())
#   arr = list(map(int, input().split()))
#   new_list = []
#   lv = []
#   while(arr):
#     M = max(arr)
#     arr.remove(M)
#     if len(new_list) == 0:
#       new_list.append(M)
#     else:
#       N = max(new_list[0], new_list[-1])
#       # print(M)
#       # print(N)
#       lv.append(N-M)
#       if new_list[0] > new_list[-1]:
#         new_list.insert(0, M)
#       else:
#         new_list.append(M)
#       # print("new_list : ",new_list)
#   print(max(lv))

T=int(input())

for i in range(T):
    N=int(input())
    trees=list(map(int,input().split()))
    trees.sort()
    result=0
    for j in range(2, N):
        result=max(result,abs(trees[j]-trees[j-2]))
    print(result)
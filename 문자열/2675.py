n=int(input())
for i in range(n):
  a,b = input().split()
  a = int(a)
  ans = ""
  for i in b:
    ans = ans + i * a
  print(ans)

# 처음 작성한 코드 
# for i in a:
#   ans = ans + b[i]*a
# 문자열 길이만큼이니까 for문에 a가 아닌 b의 길이가 들어가야하고 
# list나 array가 아니니까 b[i] 이렇게는 쓸 수 없느건가 
# 문자열은 len(b)이나 range(b) 이렇게 안해도 길이로 들어갈 수 있구나 
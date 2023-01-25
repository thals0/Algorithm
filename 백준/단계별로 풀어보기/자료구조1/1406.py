import sys
# input = sys.stdin.readline

# # 시간초과
# str = input()
# n = int(input())
# cursor = len(str)

# for _ in range(n):
#   cmd = input().split()
#   if cmd[0] == "L" and cursor != 0:
#     cursor -=1
#   elif cmd[0] == "D" and cursor != n:
#     cursor +=1
#   elif cmd[0] == "B":
#     # remove
#     str = str[:cursor-1]+str[cursor:]
#     cursor -= 1
#   elif cmd[0] == "P":
#     # insert
#     str = str[:cursor]+ cmd[1] + str[cursor:]
#     cursor += 1

# print(str)

# 시간초과 안나는 풀이 
st1 = list(input())
st2 = []
n = int(input())
for _ in range(n):
  cmd = sys.stdin.readline().split()
  if cmd[0] == 'L':
    if st1:
      st2.append(st1.pop())
  elif cmd[0] == 'D':
    if st2:
      st1.append(st2.pop())
  elif cmd[0] == 'B':
    if st1:
      st1.pop()
  else:
    st1.append(cmd[1])
# print(st1)
# print(st2)
st1.extend(reversed(st2))
print(''.join(st1))

# import sys

# stack_l = list(input())
# stack_r = []
# n = int(input())

# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0] == "L" and stack_l:
#         stack_r.append(stack_l.pop())
#     elif command[0] == "D" and stack_r:
#         stack_l.append(stack_r.pop())
#     elif command[0] == "B" and stack_l:
#         stack_l.pop()
#     elif command[0] == "P":
#         stack_l.append(command[1])

# print("".join(stack_l + list(reversed(stack_r))))
croa=['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
# cnt=0
# for i in croa:
#   for j in word:
#     if i in j:
#       cnt +=1
#     else:
#       cnt +=1
for i in croa:
  word = word.replace(i,'*')
print(len(word))
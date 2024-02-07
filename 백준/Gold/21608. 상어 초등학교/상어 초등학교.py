import sys
from collections import defaultdict

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(sys.stdin.readline())
seats = [[0] * n for _ in range(n)]
students = [list(map(int, sys.stdin.readline().split())) for _ in range(n ** 2)]
friends = defaultdict(set)
for student in students:
    me = student[0]
    friends[me] = set(student[1:])
    possible = []
    for x in range(n):
        for y in range(n):
            if not seats[x][y]:
                empty = 0
                friend = 0
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0 <= nx < n and 0 <= ny < n:
                        if not seats[nx][ny]:
                            empty += 1
                        if seats[nx][ny] in friends[me]:
                            friend += 1
                possible.append((friend, empty, x, y))
    possible.sort(key=lambda k: (-k[0], -k[1], k[2], k[3]))
    _, _, x, y = possible[0]
    seats[x][y] = me

answer = 0
for x in range(n):
    for y in range(n):
        me = seats[x][y]
        friend = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if seats[nx][ny] in friends[me]:
                    friend += 1
        if friend:
            answer += 10 ** (friend - 1)

print(answer)
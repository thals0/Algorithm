def solution(array, commands):
    answer = []
    for command in commands:
        # command[0] = 2, command[1] = 5
        arr = sorted(array[command[0]-1:command[1]])
        answer.append(arr[command[2]-1])
    return answer
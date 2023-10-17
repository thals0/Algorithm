def solution(numbers, hand):
    answer = ''
    keypad={
        1:(3,0), 2:(3,1), 3:(3,2),
        4:(2,0), 5:(2,1), 6:(2,2),
        7:(1,0), 8:(1,1), 9:(1,2),
        "*":(0,0), 0:(0,1), "#":(0,2)
    }
    
    l_pos=keypad["*"]
    r_pos=keypad["#"]
    
    for num in numbers:
        num_pos = keypad[num]
        if num in [1,4,7]:
            answer += 'L'
            l_pos = num_pos
        elif num in [3,6,9]:
            answer += 'R'
            r_pos = num_pos
        else:
            l_dis = abs(num_pos[0] - l_pos[0]) + abs(num_pos[1] - l_pos[1])
            r_dis = abs(num_pos[0] - r_pos[0]) + abs(num_pos[1] - r_pos[1])
            if l_dis < r_dis:
                answer += 'L'
                l_pos = num_pos
            elif r_dis < l_dis:
                answer += 'R'
                r_pos = num_pos
            else:
                if hand == "right":
                    answer += 'R'
                    r_pos = num_pos
                else:
                    answer += 'L'
                    l_pos = num_pos
    return answer
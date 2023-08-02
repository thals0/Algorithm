def solution(n, lost, reserve):
    answer = 0
    students, rent  = [1]*(n+1), [0]*(n+2)
    students[0],rent[0] = 3,3
    
    for lo in lost:
        students[lo] = 0
    for re in reserve:
        rent[re] = 1
        
    for i in range(1,n+1):
        if students[i] == 0:
            if rent[i] == 1: #본인이 여분을 가지고 있었을 경우
                rent[i] = 0 
                students[i] =1
            elif rent[i-1] == 1 and students[i-1] != 0: 
                rent[i-1] = 0
                students[i] =1
            elif rent[i+1] == 1 and students[i+1] != 0:
                rent[i+1] = 0
                students[i] =1
                
    for student in students:
        if student == 1:
            answer += 1
    return answer
def solution(answers):
    answer = []
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2, cnt3 = 0,0,0
    for i in range(len(answers)):
        if arr1[i%5] == answers[i]:
            cnt1 += 1
        if arr2[i%8] == answers[i]:
            cnt2 += 1
        if arr3[i%10] == answers[i]:
            cnt3 += 1
    if max(cnt1, cnt2, cnt3) == cnt1:
        answer.append(1)
    if max(cnt1, cnt2, cnt3) == cnt2:
        answer.append(2)
    if max(cnt1, cnt2, cnt3) == cnt3:
        answer.append(3)
    return answer
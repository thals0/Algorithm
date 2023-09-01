def solution(s):
    answer = []
    dict = {}
    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = [i]
            answer.append(-1)
        else:
            answer.append(i - dict[s[i]][-1])
            dict[s[i]].append(i)
    return answer
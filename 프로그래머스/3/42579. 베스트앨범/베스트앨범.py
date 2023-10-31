def solution(genres, plays):
    answer = []
    dict = {}
    tmp = {}
    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [[i,plays[i]]]
        else:
            dict[genres[i]].append([i,plays[i]]) 
    
    for i in range(len(genres)):
        if genres[i] not in tmp:
            tmp[genres[i]] = plays[i]
        else:
            tmp[genres[i]] += plays[i]
    sorted_tmp = sorted(tmp.items(), key = lambda item: item[1], reverse = True)
    
    for i in sorted_tmp:
        ls = dict[i[0]]
        ls.sort(key = lambda item: item[1], reverse=True)
        answer.append(ls[0][0])
        if len(ls) != 1:
            answer.append(ls[1][0])
    return answer
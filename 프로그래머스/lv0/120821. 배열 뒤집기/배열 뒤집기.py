def solution(num_list):
    ans = []
    for i in range(len(num_list)-1, -1, -1):
        ans.append(num_list[i])
    return ans
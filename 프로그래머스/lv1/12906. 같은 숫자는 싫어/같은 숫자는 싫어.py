def solution(arr):
    li=[]
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            li.append(arr[i]) 
    li.append(arr[-1])
    return li
            
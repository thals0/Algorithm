def solution(n, times):
    answer = 0
    times.sort()
    start = times[0]
    end = times[-1]*n
    while(start <= end):
        mid = (start+end) // 2
        sum = 0
        for time in times:
            sum += mid//time
        if sum < n:
            start = mid+1
        else:
            end = mid-1
            answer = mid
    return answer
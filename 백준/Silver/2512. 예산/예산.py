n = int(input())
req = list(map(int,input().split()))
budget = int(input())

if sum(req) <= budget:
    print(max(req))
    exit()

start = 0
end = max(req)

candidate = []
while start < end-1:
    mid = (start+end)//2
    req_sum = 0
    for r in req:
        if mid > r:
            req_sum += r
        else:
            req_sum += mid
    if req_sum > budget:
        end = mid
    if req_sum == budget:
        print(mid)
        exit()
    if req_sum < budget:
        candidate.append(mid)
        start = mid

if candidate: print(max(candidate))

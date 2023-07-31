def solution(n):
    answer = 0
    binaryNum = format(n, 'b')
    while(True):
        n += 1
        bi = format(n, 'b')
        if binaryNum.count('1') == bi.count('1'):
            return n
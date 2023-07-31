def solution(n):
    answer = 0
    binaryNum = format(n, 'b')
    while(True):
        n += 1
        bi = format(n, 'b')
        if str(binaryNum).count('1') == str(bi).count('1'):
            return n
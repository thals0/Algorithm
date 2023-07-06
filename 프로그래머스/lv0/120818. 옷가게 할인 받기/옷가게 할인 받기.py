def solution(price):
    answer = 0
    if 100000 <= price < 300000:
        # 5
        answer = int(price * 0.95)
    elif 300000 <= price < 500000:
        # 10
        answer = int(price * 0.90)
    elif 500000 <= price:
        # 20
        answer = int(price * 0.8)
    else:
        answer = price
    return answer
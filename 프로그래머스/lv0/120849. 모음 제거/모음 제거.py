def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    
    for char in my_string:
        if char not in vowels:
            answer += char
    
    return answer
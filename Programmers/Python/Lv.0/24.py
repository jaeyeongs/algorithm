# 이어 붙인 수

def solution(num_list):
    even = ''
    odd = ''
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    return int(even) + int(odd)
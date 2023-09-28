# 원소들의 곱과 합

def solution(num_list):
    multi = num_list[0]
    add = num_list[0]
    for num in num_list[1:]:
        multi *= num
        add += num
    return 1 if multi < add**2 else 0
# 등차수열의 특정한 항만 더하기 -> 이해 못한 문제

def solution(a, d, included):
    new_list = []
    new_list.append(a)
    for i in range(len(included) - 1):
        new_list.append(new_list[-1] + d)

    answer = 0
    for j, k in zip(new_list, included):
        if k:
            answer += j
    return answer
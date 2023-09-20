# 코드 처리하기 -> 이해 못한 문제

def solution(code):
    mode = False
    ret = ''
    for index, char in enumerate(code):
        if char == '1':
            mode = not mode
        else:
            ret += char if index % 2 == int(mode) else ''
    return ret if len(ret) else 'EMPTY'
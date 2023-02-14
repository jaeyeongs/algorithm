# 새 딕셔너리를 만들어서 반환

def mkDict(keys, values):
    if len(keys) != len(values):
        print('key리스트와 value리스트의 길이가 다릅니다!')
        return

    newDict = dict()
    for i, key in enumerate(keys):
        newDict[key] = values[i]

    return newDict

keys = ['오징어', '꼴뚜기', '대구', '명태']
values = [2000, 3000, 2000, 1000]
dic = mkDict(keys, values)
print(dic)
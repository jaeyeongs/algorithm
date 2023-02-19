# 리스트에서 해당 데이터의 index를 찾는 함수

def findIndex(list, value):
    for i , in_list in enumerate(list):
        try:
            in_list.index(value)
            return i
        except:
            continue

    return -1

index = findIndex([[1,2], [3,5], [100,2], [4,6]], 100)
print("100은 %d번째 index입니다." % index)
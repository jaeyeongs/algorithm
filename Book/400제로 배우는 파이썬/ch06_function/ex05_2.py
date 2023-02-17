# 가변 매개변수와 리스트 데이터 return

def mkVerticalTotal(*scoreList):
    totalList = []
    for list in scoreList:
        for i, score, in enumerate(list):
            try:
                totalList[i] += score
            except:
                totalList.append(score)

    return totalList

totalList = mkVerticalTotal([60, 60, 60], [90, 90, 90], [30, 30, 30, 100])
print(totalList)
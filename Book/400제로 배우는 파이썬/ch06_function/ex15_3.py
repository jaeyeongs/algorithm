# 람다 함수로 리스트 요소 정렬하기

fishlist = ['갑오징어', '꼴두기', '복', '명태', '바다거북이']
fishlist.sort(key = lambda x:len(x))
print("fishlist => ", fishlist)
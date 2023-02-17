# 딕셔너리 가변 인수

def showDictArgs(**dictArgs):
    print(dictArgs.values())
    keys = dictArgs.keys()
    for key in keys:
        print(key, ":", dictArgs[key])

showDictArgs(name="HONG", age=25, address="Seoul Korea")
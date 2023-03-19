# raise를 이용해 사용자 정의 예외를 강제로 발생시키는 예제

class UserDefinitionError(Exception):
    pass

try:
    raise UserDefinitionError("User definition error!")
except UserDefinitionError as e:
    print(e)
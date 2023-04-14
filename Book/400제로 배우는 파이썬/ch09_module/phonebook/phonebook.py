# 모듈을 불러서 사용할 메인 파일

from ch09_module.phonebook.phonebook_menu import *


'''메인 함수 선언'''
def main():
    while True:
        print("{:=^40}".format("주소록"))
        no = menu()


        run(no)
        print("\n")

if __name__ == '__main__':
    main()
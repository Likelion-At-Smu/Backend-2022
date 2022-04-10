import sys

def print_menue():
    print("-"*14+chr(0x1F981)+" 멋쟁이 사자처럼 전화번호부 "+chr(0x1F981)+"-"*14)
    print("-"*10+"1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료"+"-"*10)
    print("-"*53)
    print()
    print("원하시는 메뉴를 입력해주세요: ",end="")

def add():
    print("이름을 입력해주세요 : ",end="")
    name = input()
    print(name+"님의 번호를 입력해주세요 : ",end="")
    num = input()
    print(name+"님의 메일를 입력해주세요 : ",end = "")
    mail = input()
    phone_book[name]={"이름":name,"전화번호":num,"메일":mail}
    print()

def search():
    print("조회를 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    if name in phone_book:
        print(phone_book[name])
    print()


def adjustment():
    print("수정을 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    print("수정을 원하는 항목과 이름을 입력해주세요 : ",end="")
    inf = list(sys.stdin.readline().split())
    phone_book[name][inf[0]]=inf[1]
    print()

def delete():
    print("삭제를 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    del phone_book[name]
    print()


if __name__=="__main__":
    phone_book={}
    while True:
        print_menue()
        cmd = input()
        if cmd == '1':
            add()
            continue
        elif cmd == '2':
            search()
            continue
        elif cmd == '3':
            adjustment()
            continue
        elif cmd == '4':
            delete()
            continue
        elif cmd == 'q':
            break
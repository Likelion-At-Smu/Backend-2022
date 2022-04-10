def print_menue():
    print(chr(0x1F981))
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
    key, value = input().split()
    if name in phone_book:
        phone_book[name][key]=value
    if key=="이름":
        phone_book[key]=phone_book[name]
        del phone_book[name]
    print()

def delete():
    print("삭제를 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    if name in phone_book:
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
            try:
                adjustment()
                continue
            # 에러가 발생할 가능성이 있는 코드
            except Exception as ex: # 에러 종류
                print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수
            
        elif cmd == '4':
            delete()
            continue
        elif cmd == 'q':
            break

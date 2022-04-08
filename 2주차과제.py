# 2주차과제 - 전화번호부 만들기

def intro() :
    print("\n---------🦁 멋쟁이 사자처럼 전화번호부 🦁---------")
    print("------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료------")
    print("--------------------------------------------------\n")

def add() :
    phoneBook.append({'이름':'','전화번호':'','메일':''})
    name = input("이름을 입력해주세요: ")
    pNumber = input(name + "님의 번호를 입력해주세요: ") 
    mail = input(name + "님의 메일을 입력해주세요: ")
    phoneBook[-1]['이름'] = name
    phoneBook[-1]['전화번호'] = pNumber
    phoneBook[-1]['메일'] = mail

def check() :
    name = input("조회를 원하는 이름을 입력해주세요: ")
    for x in phoneBook :
        if x['이름'] == name :
            print(x)

def update() :
    name = input("수정을 원하는 이름을 입력해주세요: ")
    item, updateInfo = input("수정을 원하는 항목과 이름을 입력해주세요: ").split()
    for x in phoneBook :
        if x['이름'] == name :
            x[item] = updateInfo
        
def delete() :
    name = input("삭제를 원하는 이름을 입력해주세요: ")
    for x in phoneBook :
        if x['이름'] == name :
            phoneBook.remove(x)

phoneBook = []

while True :
    intro()
    n = input("원하시는 메뉴를 입력해주세요: ")
    if n == "q" :
        break 
    elif n == "1" :
        add()
    elif n == "2" :
        check()
    elif n == "3" :
        update()
    elif n == "4" :
        delete()
    elif n == "q" :
        break 
phonebook=[]

def default():
    print("-----------멋쟁이 사자처럼 전화전호부-----------")
    print("-----1) 추가 2) 조회 3) 수정 4) 삭제 q)종료-----")
    print("------------------------------------------------")
    print()

def add():
    name = input("이름을 입력해주세요: ")
    phone = input(name+"님의 번호를 입력해주세요: ")
    email = input(name+"님의 메일을 입력해주세요: ")
    phonebook.append({"이름":name, "전화번호":phone, "메일":email})

def inquiry():
    name = input("조회를 원하는 이름을 입력해주세요: ")
    num = 0
    if len(phonebook)!=0:
        for x in phonebook:
            if x["이름"]==name:
                print(x)
                num = 1
    if num==0:
        print("존재하지 않은 이름입니다.")

def edit():
    name = input("수정을 원하는 이름을 입력해주세요: ")
    num = 0
    for x in phonebook:
        if x["이름"]==name:
            item1, item2 = input("수정을 원하는 항목과 이름을 입력해주세요: ").split()
            x[item1]=item2
            num = 1
    if num == 0:
        print("존재하지 않은 이름입니다.")

def delete():
    name = input("삭제를 원하는 이름을 입력해주세요: ")
    for x in phonebook:
        if x["이름"]==name:
            phonebook.remove(x)
    
while True:
    default()    
    num = input("원하시는 메뉴를 입력해주세요: ")
    if num == "q":
        print()
        break
    elif num == "1":
        add()
        print()
    elif num == "2":
        inquiry()
        print()
    elif num == "3":
        edit()
        print()
    elif num == "4":
        delete()
        print()
    else:
        print("올바르지 않은 입력입니다.")

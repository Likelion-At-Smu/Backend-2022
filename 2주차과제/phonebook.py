print("1)추가 2)조회 3) 수정 4) 삭제 q) 종료")

phonelist = []

def find():
    searchname = input("조회를 원하는 이름을 입력해주세요 : ")
    searchlist = (item for item in phonelist if item['이름'] == searchname)
    dict = next(searchlist, False)
    print(dict)

while True:
    menu = input("원하시는 메뉴를 입력해주세요 : ")

    if menu == '1':
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님 번호를 입력해주세요 : ")
        mail = input(name + "님 메일을 입력해주세요 : ")
        phonelist.append({"이름": name, "번호": number, "메일": mail})

    elif menu == '2':
        searchname = input("조회를 원하는 이름을 입력해주세요 : ")
        for x in phonelist :
            if x["이름"] == searchname:
                print(x)
    elif menu == '3':
        fixname = input("수정을 원하는 이름을 입력해주세요 : ")
        fixcategory, fixcontext = input("수정을 원하는 목록과 내용을 입력하세요 : ").split()
        for x in phonelist:
            if x["이름"] == fixname:
                x[fixcategory] = fixcontext

    elif menu == '4':
        delname = input("삭제를 원하는 이름을 입력해주세요 : ")
        for x in phonelist:
            if x["이름"] == delname:
                phonelist.remove(x)
    elif menu == 'q':
        break






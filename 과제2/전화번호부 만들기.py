book=[]

def ph_book():
    print("--------------@ 멋쟁이" "사자처럼" "전화번호부--------------")
    print("----------1)" " 추가" "2)" " 조회" "3)" " 수정" "4)" " 삭제" "q)" " 종료----------")
    print("------------------------------------------------------")


def insert():
    name = input("이름을 입력해주세요: ")
    phnum = input("이현우님의 번호를 입력해주세요: ")
    mail = input("이현우님의 메일을 입력해주세요: ")
    print("\n")

    book.append({"이름" : name, "전화번호": phnum, "메일": mail })

def search():   #조회 함수
    name = input("조회를 원하는 이름을 입력해주세요 : ")
    
    for i in book:  # book 리스트 내부에서 찾아오는 loop
        print(book)
    print("\n")

def fix():
    name = input("수정을 원하는 이름을 입력해주세요 : ")
    what, likethis = input("수정을 원하는 항목과 이릉을 입력해주세요: ").split()

    for x in book:  # book 리스트 내부에서 찾아오는 loop
        x[what] = likethis
    print("\n")

def delete():
    global set_book
    name = input("삭제를 원하는 이름을 입력해주세요: ")
    book.clear()    
    # for x in book:
    #     x['이름'] = None
    print("\n")


set_book = set(book)
while True:
    ph_book()
    num = input("원하시는 메뉴를 입력해주세요: ")
    if num == "1":
        insert()
    elif num == "2":
        search()
    elif num == "3":
        fix()
    elif num == "4":
        delete()
    elif num == "q":
        break
    else:
        print("잘못된 값을 입력하였습니다")
        


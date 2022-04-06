intro = "--------------🦁 멋쟁이 사자처럼 전화번호부 🦁--------------\n" \
        "----------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료----------\n" \
        "------------------------------------------------------"
phone_book = []

while True:
    print("\n" + intro + "\n")
    question = input("원하는 메뉴를 입력해주세요 : ")
    if question == "q":
        break

    elif question == "1":
        phone_book.append({"이름": "", "전화번호": "", "메일": ""})
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님의 번호를 입력해주세요 : ")
        mail = input(name + "님의 메일을 입력해주세요 : ")
        phone_book[-1]["이름"] = name
        phone_book[-1]["전화번호"] = number
        phone_book[-1]["메일"] = mail

    elif question == "2":
        name = input("조회를 원하는 이름을 입력해주세요 : ")
        for i in phone_book:
            if i["이름"] == name:
                print(i)
            else:
                continue

    elif question == "3":
        name = input("수정을 원하는 이름을 입력해주세요 : ")
        qType, edit = input("수정을 원하는 항목과 이름을 입력해주세요 : ").split()
        for i in phone_book:
            if i["이름"] == name:
                i[qType] = edit

    elif question == "4":
        name = input("삭제를 원하는 이름을 입력해주세요 : ")
        for i in phone_book:
            if i["이름"] == name:
                i.pop("이름")
                i.pop("전화번호")
                i.pop("메일")

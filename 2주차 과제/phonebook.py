phonebook = []
# 이름으로 전화번호 추가
def insert_phonebook():
    new_dict={"이름":"", "전화번호":"", "메일":""}
    new_dict["이름"]=input("이름을 입력해주세요: ")
    new_dict["전화번호"]=input(f"{new_dict.get('이름')}님의 전화번호를 입력해주세요: ")
    new_dict["메일"] = input(f"{new_dict.get('이름')}님의 메일을 입력해주세요: ")
    phonebook.append(new_dict)

# 이름으로 전화번호 조회
def read_phonebook():
    read_name = input("조회를 원하는 이름을 입력해주세요: ")
    exist = False
    for i in phonebook:
        if i["이름"] == read_name:
            exist = True
            print(i)
    if exist == False:
        print("해당 이름은 전화번호부에 존재하지 않습니다.")

#이름으로 저장된 요소 수정
def update_phonebook():
    update_name = input("수정을 원하는 이름을 입력해주세요: ")
    for i in phonebook:
        if i["이름"] == update_name:
            update_key, update_value = input("수정을 원하는 항목과 내용을 입력해주세요: ").split()
            i[update_key] = update_value
        break

#이름으로 저장된 요소 삭제
def delete_phonebook():
    delete_name = input("삭제를 원하는 이름을 입력해주세요: ")
    for i in phonebook[:]:
        if i["이름"] == delete_name:
            phonebook.remove(i)

if __name__ == '__main__':
    while True:
        print("")
        print("---------------멋쟁이 사자처럼 전화번호부---------------")
        print("---------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료--------")
        print("--------------------------------------------------")
        print("")
        sel_menu = input("원하시는 메뉴를 입력해주세요: ")
        if sel_menu == "1":
            insert_phonebook()
        elif sel_menu == "2":
            read_phonebook()
        elif sel_menu == "3":
            update_phonebook()
        elif sel_menu == "4":
            delete_phonebook()
        elif sel_menu == "q":
            break
        else:
            print("잘못 입력하였습니다.")
    print("전화번호부를 종료합니다.")

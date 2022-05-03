import json
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import re


phonebook = []

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("id","ps")
reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"


def make_rank_file():
    driver = webdriver.Chrome('/Users/choisemin/Desktop/workspace/chromedriver')
    url = "http://www.daum.net/"
    driver.get(url)
    time.sleep(1)
    html = driver.page_source


    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll('a','link_favorsch')
    rank = 1

    search_rank_file = open("rankresult.text", "w")

    for result in results:
        search_rank_file.write(str(rank)+"위: "+result.text+"\n")
        rank += 1

    search_rank_file.close()

def weaherinfo():
    city = "Seoul"
    apikey = "16a4f1b45c2860f0730a00b54dae429c"
    lang = 'kr'
    units = 'metric'
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}"

    weather = requests.get(api).text
    data = json.loads(weather)
    content = f"""{data["name"]}의 날씨입니다.\n날씨는 {data["weather"][0]["main"]}입니다.\n현재 온도는 {data["main"]["temp"]}도 입니다.\n하지만 체감 온도는 {data["main"]["feels_like"]}도 입니다."""
    return content


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

def send_mail():
    dest_name = input("전송을 원하는 상대방의 이름을 입력해주세요: ")
    for i in phonebook:
        if i["이름"] == dest_name:
            email = i["메일"]
            if bool(re.match(reg, email)):
                message = EmailMessage()
                message.set_content(weaherinfo())
                message["Subject"] = "최세민 과제#3 제출입니다!"
                message["From"] = "id"
                message["To"] = email

                make_rank_file()
                with open("rankresult.text", "rb") as text:
                    rank_text = text.read()

                message.add_attachment(rank_text, maintype='text', subtype='txt', filename=text.name)

                smtp.send_message(message)
                print("정상적으로 메일이 발송되었습니다.")
            else:
                print("유효한 이메일 주소가 아닙니다.")


while True:
    print("")
    print("---------------------멋쟁이 사자처럼 전화번호부---------------------")
    print("---------1) 추가 2) 조회 3) 수정 4) 삭제 5)메일 전송 q) 종료--------")
    print("-------------------------------------------------------------")
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
    elif sel_menu == "5":
        send_mail()
    elif sel_menu == "q":
        break
    else:
        print("잘못 입력하였습니다.")
smtp.quit()
print("전화번호부를 종료합니다.")

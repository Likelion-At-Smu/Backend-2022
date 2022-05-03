from email.message import EmailMessage
import smtplib
import requests
import json
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


# 이메일 유효성 검사 함수
def is_valid(addr):
    if re.match('(^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$)', addr):
        return True
    else:
        return False


# 크롤링 API
def save_fav(url, tag, class_name, chrome_driver_path):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url=url)
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    rank = 1

    results = soup.findAll(tag, class_name)

    search_rank_file = open("rankresult.txt", "a")

    # 실시간 검색어 txt 파일 만들기
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
        rank += 1


# 날씨
city = "Seoul"
apikey = "1cf8ec3373ffb1bd6bc4b12767ebcbb6"
lang = "kr"
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
data = json.loads(result.text)

location = data["name"]
weather_description = data["weather"][0]["description"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

weather = f"{location}의 날씨입니다.\n날씨는 {weather_description}입니다.\n현재 온도는 {temp}입니다.\n하지만 체감 온도는 {feels_like}입니다."

phonebook = []


def default():
    print("-----------멋쟁이 사자처럼 전화전호부-----------")
    print("-----1) 추가 2) 조회 3) 수정 4) 삭제 5) 메일 전송 q)종료-----")
    print("------------------------------------------------")
    print()


def add():
    name = input("이름을 입력해주세요: ")
    phone = input(name + "님의 번호를 입력해주세요: ")
    email = input(name + "님의 메일을 입력해주세요: ")
    phonebook.append({"이름": name, "전화번호": phone, "메일": email})


def inquiry():
    name = input("조회를 원하는 이름을 입력해주세요: ")
    num = 0
    if len(phonebook) != 0:
        for x in phonebook:
            if x["이름"] == name:
                print(x)
                num = 1
    if num == 0:
        print("존재하지 않은 이름입니다.")


def edit():
    name = input("수정을 원하는 이름을 입력해주세요: ")
    num = 0
    for x in phonebook:
        if x["이름"] == name:
            item1, item2 = input("수정을 원하는 항목과 이름을 입력해주세요: ").split()
            x[item1] = item2
            num = 1
    if num == 0:
        print("존재하지 않은 이름입니다.")


def delete():
    name = input("삭제를 원하는 이름을 입력해주세요: ")
    for x in phonebook:
        if x["이름"] == name:
            phonebook.remove(x)


def mail():
    name = input("메일 전송을 원하는 사람의 이름을 입력해주세요: ")
    for x in phonebook:
        if x["이름"] == name:
            mail = x["메일"]

        save_fav("https://www.daum.net/", "ul", "list_favorsch", "C:\\Users\\unhi0\\OneDrive\\바탕 화면\\멋사\\Backend-2022\\과제3\\chromedriver.exe")

        with open("rankresult.txt", "rb") as file:
            text_file = file.read()

        message = EmailMessage()
        message.set_content(weather)
        message.add_attachment(text_file, maintype='text', subtype='txt', filename = file.name)

        message["Subject"] = "박은희 과제3 제출합니다!"
        message["From"] = "unhipark000@gmail.com"
        message["To"] = mail

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login("unhipark000@gmail.com", "vazbvxltwvpfxcpc")

        is_valid(mail)
        if smtp.send_message(message) == {}:
            print("파일 저장이 완료되었습니다. \n정상적으로 메일을 보냈습니다.")

        smtp.quit()


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
    elif num == "5":
        mail()
        print()
    else:
        print("올바르지 않은 입력입니다.")

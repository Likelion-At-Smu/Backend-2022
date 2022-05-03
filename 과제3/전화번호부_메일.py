import os
print(os.getcwd())
import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.message import EmailMessage
import re
from selenium import webdriver


# # 크롤링 api  url, tag, class_name, chrome_driver_path
def save_fav():
    driver = webdriver.Chrome('D:\OneDrive\pythonProject\chromedriver')
    url = "http://www.daum.net/"
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    rank = 1
    results = soup.findAll('a', 'link_favorsch')
    search_rank_file = open("rankresult.text", "w")

    # 실시간 검색어 txt 파일 만들기

    for result in results:
        search_rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
        rank += 1
    search_rank_file.close()



def _weahter():
    city = "seoul"
    apikey = "16e6ac07d633d3eb38dfea2054437c36"
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

    result = requests.get(api)
    data = json.loads(result.text)
    content = f"""{data["name"]}의 날씨입니다.\n날씨는 {data["weather"][0]["main"]}입니다.\n현재 온도는 {data["main"]["temp"]}도 입니다.\n하지만 체감 온도는 {data["main"]["feels_like"]}도 입니다."""
    return content


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("id", "ps")
reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"


book = []


def ph_book():
    print("--------------@ 멋쟁이" "사자처럼" "전화번호부--------------")
    print("----------1)" " 추가" "2)" " 조회" "3)" " 수정" "4)" " 삭제" "5)" "메일 전송" "q)" " 종료----------")
    print("------------------------------------------------------")


def insert():
    name = input("이름을 입력해주세요: ")
    phnum = input("번호를 입력해주세요: ")
    mail = input("메일을 입력해주세요: ")
    print("\n")

    book.append({"이름": name, "전화번호": phnum, "메일": mail})


def search():  # 조회 함수
    name = input("조회를 원하는 이름을 입력해주세요 : ")

    for i in book:  # book 리스트 내부에서 찾아오는 loop
        print(book)
    print("\n")


def fix():
    name = input("수정을 원하는 이름을 입력해주세요 : ")
    what, likethis = input("수정을 원하는 항목과 이름을 입력해주세요: ").split()

    for x in book:  # book 리스트 내부에서 찾아오는 loop
        x[what] = likethis
    print("\n")


def delete():
    global set_book
    name = input("삭제를 원하는 이름을 입력해주세요: ")
    book.clear()
    print("\n")


def send():
    sendEmail("id")
    # smtp.quit()


def sendEmail(addr):
    _name = input("메일 전송을 원하는 사람의 이름을 입력해주세요: ")
    for x in book:
        if x["이름"] == _name:
            email = x["메일"]
            if bool(re.match(reg, addr)):
                message = EmailMessage()
                message.set_content(_weahter())
                message["Subject"] = "제목없음"
                message["From"] = "id"
                message["To"] = addr
                save_fav()
                with open("rankresult.text", "rb") as text:
                    rankresult_text = text.read()
                message.add_attachment(rankresult_text, maintype='text', subtype='txt')
                smtp.send_message(message)
                print("정상적으로 메일이 발송되었습니다.")
            else:
                print("유효한 이메일 주소가 아닙니다.")


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
    elif num == "5":
        send()
    elif num == "q":
        break
    else:
        print("잘못된 값을 입력하였습니다")

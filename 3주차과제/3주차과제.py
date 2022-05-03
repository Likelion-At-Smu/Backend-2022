import requests
import json
import smtplib
from email.message import EmailMessage
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime

city = "Seoul"
apikey = "84918d9fe26e47b8fc1e4d73dd6fe2f2"
lang = "kr"
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
result = requests.get(api)
data = json.loads(result.text) # json타입으로 변경

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("id", "password")

def sendEmail(addr):
	reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.+[a-zA-Z]{2,3}$" # 정규표현식
	if bool(re.match(reg,addr)):
		smtp.send_message(message)
		print("정상적으로 메일이 발송되었습니다.")
	else:
		print("유효한 이메일 주소가 아닙니다")

cityName = data["name"]
weather = data["weather"][0]["description"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

content = f"{cityName}의 날씨입니다.\n날씨는 {weather}입니다.\n현재 온도는 {temp}입니다.\n하지만 체감 온도는 {feels_like}입니다."

message = EmailMessage()
message.set_content(content)

# 크롤링 API
def save_fav(url, tag, class_name, chrome_driver_path):
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url=url)
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    rank = 1
    results = soup.findAll(tag, class_name)

    search_rank_file = open("rankresult.txt","w")

# 실시간 검색어 txt 파일 만들기
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+ "\n")
        rank += 1


def intro() :
    print("\n---------🦁 멋쟁이 사자처럼 전화번호부 🦁---------")
    print("------1) 추가 2) 조회 3) 수정 4) 삭제 5) 메일 전송 q) 종료------")
    print("--------------------------------------------------\n")

def add() :
    phoneBook.append({'이름':'','전화번호':'','메일':''})
    name = input("이름을 입력해주세요: ")
    pNumber = input(name + "님의 번호를 입력해주세요: ")
    mail = input(name + "님의 메일을 입력해주세요: ")
    phoneBook[-1]['이름'] = name
    phoneBook[-1]['전화번호'] = pNumber
    phoneBook[-1]['메일'] = mail
    for x in phoneBook:
        if x['이름'] == name:
            print("저장이 완료되었습니다.")

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

def sendmail() :
    name = input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
    for x in phoneBook:
        if x['이름'] == name:
            mail = x['메일']
        message["Subject"] = "멋사 3주차과제 - 10기_정혜원"
        message["From"] = "hijjoy04@gmail.com"
        message["To"] = mail

        save_fav("http://www.daum.net","a","link_favorsch","/Users/noweyh/PycharmProjects/pythonProject1/lion/chromedriver")

        with open("rankresult.txt","rb") as text:
            text_file = text.read()
        message.add_attachment(text_file, maintype = 'text', subtype = 'txt', filename = text.name)

        sendEmail(mail)
        smtp.quit()


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
    elif n == "5" :
        sendmail()
    elif n == "q" :
        break

from datetime import datetime

import requests
import smtplib
from email.message import EmailMessage
import re
import json

from selenium.webdriver.chrome import webdriver
from bs4 import BeautifulSoup


city = "Seoul"
apikey = "my api is secret"
lang = "kr"
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" # ? 앞쪽은 공통내용
result = requests.get(api)
data = json.loads(result.text)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")
        
message = EmailMessage()
country = data["name"]
weather = data["weather"][0]["description"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

content = f"{country}의 날씨입니다.\n날씨는 {weather}입니다.\n현재 온도는 {temp}입니다.\n하지만 체감 온도는 {feels_like}입니다."

message.set_content(content)
message["Subject"] = "[3주차 과제] 박현빈"
message["From"] = "id"

# 크롤링 API
def save_fav(url, tag, class_name, chrome_driver_path):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url = url)
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    rank = 1

    results = soup.findAll(tag, class_name)

    search_rank_file = open("rankresult.txt","a")

    # 실시간 검색어 txt 파일 만들기
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+ "\n")
        rank += 1

phonebook = []

while True:
    print("----------멋쟁이 사자처럼 전화번호부----------")
    print("------1)추가 2)조회 3)수정 4)삭제 5)메일 전송 q)종료------")
    print("----------------------------------------------")


    menu = input("원하시는 메뉴를 입력해주세요: ")
    
    if menu == "q":
        print("Process finished with exit code 0")
        break;

    elif menu == "1":
        name = input("이름을 입력해주세요: ")
        phone = input(name+"님의 번호를 입력해주세요: ")
        mail = input(name+"님의 메일을 입력해주세요: ")
        phonebook.append({"이름":name, "전화번호":phone, "메일":mail})
    
    elif menu == "2":
        name = input("조회를 원하는 이름을 입력해주세요: ")
        for i in phonebook:
            if i["이름"] == name:
                print(i)
            else:
                print("목록에 이름이 존재하지 않습니다.")

    elif menu == "3":
        name = input("수정을 원하는 이름을 입력해주세요: ")
        item, content = input("수정을 원하는 항목과 내용을 입력해주세요: ").split()
        for i in phonebook:
            if i["이름"] == name:
                i[item] = content
    
    elif menu == "4":
        name = input("삭제를 원하는 이름을 입력해주세요: ")
        for i in phonebook:
            if i["이름"] == name:
                phonebook.remove(i)
                
    elif menu == "5":
        name = input("메일 전송을 원하는 사람의 이름을 입력해주세요: ")
        for i in phonebook:
            if i["이름"] == name:
                mail = i["메일"]
        message["To"] = mail
        
        with open("rankresult.txt","rb") as f:
            text_file = f.read()
        message.add_attachment(text_file, maintype = 'text', subtype = 'txt', filename = f.name)
        
        smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
        smtp.login("id", "pw")
        sendEmail(mail)
        smtp.quit()
    
    else:
        print("없는 메뉴입니다. 다시 선택해주세요. ")
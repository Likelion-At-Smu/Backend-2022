import requests
import json
import smtplib
from email.message import EmailMessage
import re

city = "Seoul"
apikey = "7637e7b3e9209c47cb24f8cfb3f4b15c"
lang = "kr"
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
result = requests.get(api)
data = json.loads(result.text)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
def sendEmail(addr):
    reg = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
location = data["name"]
weather_description = data["weather"][0]["description"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

content = f"{location}의 날씨입니다.\n" \
          f"날씨는 {weather_description}입니다.\n" \
          f"현재 온도는 {temp}입니다.\n" \
          f"하지만 체감 온도는 {feels_like}입니다."

message.set_content(content)
message["Subject"] = "멋사_3주차_과제_박수진"
message["From"] = "tnwlssla20@gmail.com"


intro = "--------------🦁 멋쟁이 사자처럼 전화번호부 🦁--------------\n" \
        "----------1) 추가 2) 조회 3) 수정 4) 삭제 5) 메일 전송 q) 종료----------\n" \
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
        for i in phone_book:
            if i["이름"] == name:
                print("저장이 완료되었습니다.")

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
                phone_book.remove(i)

    elif question == "5":
        name = input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
        for i in phone_book:
            if i["이름"] == name:
                mail = i["메일"]
        message["To"] = mail

        # 실시간 검색어가 폐지돼서 네이버 상단바 목록을 크롤링했습니다.
        with open("rankresult.txt", "rb") as f:
            text_file = f.read()
        message.add_attachment(text_file, maintype='text', subtype='txt', filename= f.name)

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login("tnwlssla20@gmail.com", "aeaggowisdevimcx")
        sendEmail(mail)
        smtp.quit()



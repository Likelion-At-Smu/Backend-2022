import txt as txt
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
import smtplib
from email.message import EmailMessage
import imghdr
import re
import os
import smtplib
import selenium
from selenium import webdriver

print("1)추가 2)조회 3) 수정 4) 삭제 5)메일보내기 q) 종료")

phonelist = []


# def find():
# searchname = input("조회를 원하는 이름을 입력해주세요 : ")
# searchlist = (item for item in phonelist if item['이름'] == searchname)
# dict = next(searchlist, False)
# print(dict)


def save_fav(url):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url=url)
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    print(soup)
    rank = 1

    results = soup.findAll('div', "slide_favorsch")

    search_rank_file = open("rankresult.txt", "a")

    # 실시간 검색어 txt 파일 만들기
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
        rank += 1


while True:
    menu = input("원하시는 메뉴를 입력해주세요 : ")

    if menu == '1':
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님 번호를 입력해주세요 : ")
        mail = input(name + "님 메일을 입력해주세요 : ")
        phonelist.append({"이름": name, "번호": number, "메일": mail})

    elif menu == '2':
        searchname = input("조회를 원하는 이름을 입력해주세요 : ")
        for x in phonelist:
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
    elif menu == '5':
        mailname = input("메일 전송을 원하는 이름을 입력해주세요 : ")
        for x in phonelist:
            if x["이름"] == mailname:
                save_fav('https://www.daum.net/')

                city = "Seoul"
                apikey = "ba7fa79390699019eec02a9122d14965"
                api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

                result = requests.get(api)

                data = json.loads(result.text)

                SMTP_SERVER = "smtp.gmail.com"
                SMTP_PORT = 465


                def sendEmail(addr):
                    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
                    if bool(re.match(reg, addr)):
                        smtp.send_message(message)
                        print("정상적으로 메일이 발송되었습니다.")
                    else:
                        print("유효한 이메일 주소가 아닙니다.")


                message = EmailMessage()
                message.set_content(data["name"] + "의 날씨입니다.\n" + "날씨는 " + data["weather"][0]["main"] + "입니다.\n" + "현재 "
                                                                                                                   "온도는"
                                                                                                                   " "
                                    + str(data["main"]["temp"]) + "입니다.\n" + "하지만 체감 온도는 " + str(data["main"]["feels_like"]) +
                                    "입니다.")

                message["Subject"] = "테스트용 메일."
                message["From"] = "yj07459@gmail.com"
                message["To"] = "khs8196@gmail.com"

                with open("rankresult.txt", "rb") as text:
                    text_file = text.read()

                message.add_attachment(text_file, maintype='text', subtype='txt', filename=text.name)

                smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
                smtp.login("id", "pw")
                # 메일을 보내는 sendEmail 함수를 호출해서 실행해보기
                sendEmail(x["메일"])
                smtp.quit()



    elif menu == 'q':
        break

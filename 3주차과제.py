
import sys
import io
from typing import Text
import requests
import json
import smtplib
from email.message import EmailMessage
import re
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

city = "Seoul"
apikey = "246cd9fc7ce04d457364184f763e7e92"
lang = "kr"
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
data = json.loads(result.text)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
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
message["From"] = "jomulagy688@gmail.com"

url = "http://www.daum.net"

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
def print_menue():
    print(chr(0x1F981))
    print("-"*14+chr(0x1F981)+" 멋쟁이 사자처럼 전화번호부 "+chr(0x1F981)+"-"*14)
    print("-"*10+"1) 추가 2) 조회 3) 수정 4) 삭제 5) 메일 전송 q) 종료"+"-"*10)
    print("-"*53)
    print()
    print("원하시는 메뉴를 입력해주세요: ",end="")

def add():
    print("이름을 입력해주세요 : ",end="")
    name = input()
    print(name+"님의 번호를 입력해주세요 : ",end="")
    num = input()
    print(name+"님의 메일를 입력해주세요 : ",end = "")
    mail = input()
    phone_book[name]={"이름":name,"전화번호":num,"메일":mail}
    print()

def search():
    print("조회를 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    if name in phone_book:
        print(phone_book[name])
    print()


def adjustment():
    print("수정을 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    print("수정을 원하는 항목과 이름을 입력해주세요 : ",end="")
    key, value = input().split()
    if name in phone_book:
        phone_book[name][key]=value
    if key=="이름":
        phone_book[key]=phone_book[name]
        del phone_book[name]
    print()

def delete():
    print("삭제를 원하는 이름을 입력해주세요 : ",end="")
    name = input()
    if name in phone_book:
        del phone_book[name]
    print()

def send_mail():
    global message
   
    print("메일 전송을 원하는 사람의 이름을 입력해주세요 : ",end="")
    name = input()
    if name in phone_book:
        mail = phone_book[name]["메일"]

    message["To"] = mail

    save_fav(url,"a", "link_favorsch")
    with open("rankresult.txt","rb") as text:
        text_file = text.read()
        print("파일 저장이 완료되었습니다.")

    message.add_attachment(text_file,maintype='text',subtype='txt',filename=text.name)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)

    smtp.login("jomulagy688@gmail.com","cbzluzodtqhtosqf")
    smtp.send_message(message)
    smtp.quit()
    print("정상적으로 메일이 발송되었습니다.")
   
def save_fav(url, tag, class_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url = url)
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    rank = 1

    results = soup.findAll(tag, class_name)

    search_rank_file = open("rankresult.txt","w")
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n".encode("unicode-escape").decode()).encode().decode('unicode-escape'))

    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+ "\n")
        rank += 1

    driver.close()

if __name__=="__main__":
    phone_book={}
    
    while True:
        print_menue()
        cmd = input()
        if cmd == '1':
            add()
            continue
        elif cmd == '2':
            search()
            continue
        elif cmd == '3':
            try:
                adjustment()
                continue
            # 에러가 발생할 가능성이 있는 코드
            except Exception as ex: # 에러 종류
                print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수
            
        elif cmd == '4':
            delete()
            continue
        elif cmd == '5':
            send_mail()
            continue
        elif cmd == 'q':
            break
        else:
            continue

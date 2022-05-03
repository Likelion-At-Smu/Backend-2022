from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

url = "http://www.daum.net"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)
response = driver.page_source.encode('utf-8', errors='replace')
soup = BeautifulSoup(response, 'html.parser')
results = soup.findAll("a", "link_favorsch")
rank = 1

search_rank_file = open("rankresult.txt","a")
search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    rank += 1
driver.close()
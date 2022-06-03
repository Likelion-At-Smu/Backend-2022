import os
import sys
import urllib.request
import json

client_id = "uNdkgaNYbwgjVy31Vudz"
client_secret = "1m_aVNcLzn"
encText = urllib.parse.quote("관상")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


resdata = response_body.decode('utf-8')

#utf-8, ascii 관련 코드는 한국어를 보기위한 설정
# with open("movie.json",'w', encoding='UTF-8-sig') as file:
#     file.write(json.dumps(resdata, ensure_ascii=False))

pydata = json.loads(resdata)
data = pydata['items']
print (data[0]['title'])
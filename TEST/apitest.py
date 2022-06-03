# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

import urllib.request
import json
# 특정 url에 request를 날릴 수 있게하는 도구
client_id = "UWN9cqEgcpa5_d2JrrkS"
client_secret = "OgFtpP1Pij"

encText = urllib.parse.quote("한국")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
#맛집을 담고 있는 url로 보내진다
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText
#요청 변수인 query를 써야한다

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
#request의 header의 최상단 부분에 client_id 와 client_secret을 붙여야한다
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
   # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

resdata = response_body.decode('utf-8')

# with open('movie.json','w',encoding='UTF-8-sig') as file: #movie.json안에 쓸거다
#     file.write(json.dumps(resdata, ensure_ascii=False)) #어떤 json 데이터를 가져와서 쓸거다
    #혹시 모르니 ascii를 false로 지정한것이다
#dump는 json 데이터를 실어주어라
#loads의 경우는 가져와라
pydata = json.loads(resdata)
data = pydata['items']

print(data[1]['title'])
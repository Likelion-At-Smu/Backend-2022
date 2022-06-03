# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

# 특정 URL에 request 날릴 수 있게 하는 도구
import urllib.request
import json

client_id = "RMge5SCepqPyOEtJZYKn"
client_secret = "MNNIBE9jja"

encText = urllib.parse.quote("한국")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText

request = urllib.request.Request(url)
# header부분에도 id와 secret을 추가해줘야 함
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)

# 우리가 보내는 request가 잘 받아졌는지의 여부를 getcode()로 받을 수 있음
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # 한글을 읽어들이기 위해서는 utf-8로 decode해야 함
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# 받은 결과를 파일로 저장
resdata = response_body.decode('utf-8')
# with open('movie.json', 'w', encoding='UTF-8-sig') as file:
#     file.write(json.dumps(resdata, ensure_ascii=False))

# json을 실어줘라 : dumps / 갖고와줘라 : loads
pydata = json.loads(resdata)
data = pydata['items']

print(data[0]['title'])
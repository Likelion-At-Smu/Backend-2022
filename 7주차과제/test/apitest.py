# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

import urllib.request # 특정 url에 requset를 넘길 수 있게
import json

client_id = "hq95aXzT7gH7woi2s5bu"
client_secret = "hJLvkb6dU7"


encText = urllib.parse.quote("어벤져스")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText

request = urllib.request.Request(url)
# 내가 누구인지를 requset객체에 포함시켜서 요청을 보내줘야함 ! 
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# 반환받는 객체 response
response = urllib.request.urlopen(request)
rescode = response.getcode() # 내가 보낸 정보가 잘 받아졌는지 확인 
if(rescode==200) : # 요청을 성공적으로 받았다면 
    response_body = response.read() 
    # print(response_body.decode('utf-8'))
else :
    print("Error Code:" + rescode)


resdata = response_body.decode('utf-8')

with open('movie.json', 'w', encoding='utf-8') as file :
    file.write(json.dumps(resdata, ensure_ascii=False)) # json.dumps(resdata) -> resdata를 가지고 옴

# json파일에서 items키가 가지는 리스트에서 원하는 정보를 빼냄
pydata = json.loads(resdata) # resdata를 가져와줘
data = pydata["items"]

print(data[0]['title'])
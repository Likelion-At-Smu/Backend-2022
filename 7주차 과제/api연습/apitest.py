# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

import urllib.request
import json

client_id = "hrraDP9IjEbIe_T7nhev"
client_secret = "RM_44NOO0Y"

encText = urllib.parse.quote("한국")#검색어
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText 

request = urllib.request.Request(url)#리퀘스트 객체를 보낸다.
request.add_header("X-Naver-Client-Id", client_id)#추가 정보가 필요하면 헤더에 정보를 붙여서 보낸다.
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()
if(rescode==200):#response로 200번은 성공코드
    response_body = response.read()
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)#다른게 오면 에러가 발생했다는 뜻

resdata = response_body.decode('utf-8')#한국말로 정보를 받으려면 이렇게 해야함

# with open('movie.json', 'w', encoding='UTF-8-sig') as file: json 데이터를 저장할거다
#     file.write(json.dumps(resdata, ensure_ascii=False))한국어를 제대로 보기위한 설정

pydata = json.loads(resdata)#json데이터를 갖고와라
data = pydata['items']

print(data[0]['title'])#첫번째 검색결과의 제목
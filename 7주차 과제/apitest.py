import os
import io
import sys
import json
# 특정 url에 request를 날리는 도구
import urllib.request

# 발급받은 계정
client_id = 'WBizd3AjzRS6rm8IoYHJ'
client_secret = 'ptArHpcM6x'

# query 변수값 설정
encText = urllib.parse.quote("한국")
# query에 매칭
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

# 영화 검색을 위한 url
url = 'https://openapi.naver.com/v1/search/movie.json?query=' + encText
# request요청
request = urllib.request.Request(url)
# request요청을 위한 인증
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
# 응답객체
response = urllib.request.urlopen(request)

rescode = response.getcode()
# 요청을 성공적으로 받았다면
if(rescode==200):
    response_body = response.read()
    # 한글을 읽어들이기 위한 과정
    print(response_body.decode('utf-8'))
# 에러가 발생했다면
else:
    print("Error Code:" + rescode)

# json file 로 저장하기
resdata = response_body.decode('utf-8')
# with io.open('movie.json', 'w', encoding = 'UTF-8-sig') as file:
#     # 응답객체를 아스키 코드를 이용해 가져온다.
#     file.write(json.dumps(resdata, ensure_ascii=False))

# resdata의 item들을 list로 받기
pydata = json.loads(resdata)

data = pydata['items']

print(data)
# 웹 스크랩핑 테스트 준비

import requests
from bs4 import BeautifulSoup

# 웹 페이지의 URL
url = 'https://www.naver.com/'

# 웹 페이지에 HTTP GET 요청을 보내고 응답을 받음
resp = requests.get(url)

html = """
<nav class = "menu-box-1" id="menu-box">
  <ul>
    <li>
      <a href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""

 # 응답 내용을 BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

print(soup.select('nav'))

# <div></div> - div 태그
# 열린태그, 닫는 태그, 구성요소 -> 엘리먼트
# div 엘리먼트

# BeautifulSoup 함수
# select()
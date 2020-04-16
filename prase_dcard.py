from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

driver = webdriver.Chrome()
url = 'https://www.dcard.tw/f'
driver.get(url)

inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('Python')

driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
# 休息兩秒 等
time.sleep(2)

html = driver.page_source
soup = bs(html, 'html.parser')

meta_datas = []
for x in soup.find_all('span', {'class':'sc-6oxm01-2 hiTIMq'}):
    meta_datas.append(x.text.strip())
print(meta_datas)

# 從meta data 裡面挑出『看板』
forums = []
author = []
times = []
for i in range(len(meta_datas)):
    if i % 3 == 0:  # 看板
        forums.append(meta_datas[i])
    if i % 3 == 1:  # 作者
       author.append(meta_datas[i])
    if i % 3 == 2:  # 時間
        times.append(meta_datas[i])

# 獲得文章標題
titles = []
for x in soup.find_all('h2',{'class':'sc-1v1d5rx-3 eihOFJ'}):
    titles.append(x.text)
print(titles)

hrefs = []
data = soup.find_all('a',{'class':'sc-1v1d5rx-4 gCVegi'})
hrefs = []
for x in data:
    hrefs.append(x['href'])

# 從相對連結及url組成絕對連結
links = []
for href in hrefs:
    links.append(urljoin(url, href))
print(links)

for i in range(len(forums)):
    if forums[i] == "軟體工程師":
        print(forums[i], titles[i], links[i])

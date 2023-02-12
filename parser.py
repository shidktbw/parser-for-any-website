import requests
from selenium import webdriver
from bs4 import BeautifulSoup

headers = {'User-Agent': 'your user-agent'}

url = input()

session = requests.Session()

response = session.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    print(text)
else:
    driver = webdriver.Edge()
    driver.get(url)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    print(text)
    driver.quit()

from bs4 import BeautifulSoup
import requests
import urllib
import uuid
from pathlib import Path
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import subprocess

outputFolder = Path("CuteGirls")
outputFolder.mkdir(exist_ok=True)
options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
url = "https://www.google.com"
keyword = "かわいい女性"
driver.get(url)
time.sleep(1)

search = driver.find_element_by_name("q")
search.send_keys(keyword)
search.submit()
time.sleep(2)

imageClassName = "hide-focus-ring"
imagePageButton = driver.find_element_by_class_name(imageClassName)
imagePageButton.click()

imageOfKeywordUrl = driver.current_url
response = requests.get(imageOfKeywordUrl)
soup = BeautifulSoup(response.content,"html.parser")
content = soup.find("div",attrs={"class:": "mJxzWe"})
with open("test.txt","wb") as file:
    file.write(content)
subprocess.run("open test.txt",shell=True)
images = content.find_all("img")

for image in images:
    longImageUrl = urllib.parse.urljoin(imageOfKeywordUrl,image["src"])
    imageData = requests.get(longImageUrl)
    with open(f"./CuteGirls/{uuid.uuid4()}/jpeg","wb") as file:
        file.write(imageData.content)
    

time.sleep(2)
driver.close()


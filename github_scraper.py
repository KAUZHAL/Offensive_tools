from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
repo = "https://github.com/KAUZHAL"
driver.get(repo)
res=driver.find_elements(By.CLASS_NAME,"repo")
links =[]
flink = []

def going_for_raw(second_page):
    driver.get(second_page)
    raw=driver.find_element(By.CLASS_NAME," ")#class name in html of tag
    raw.click()
    html=driver.page_source
    html=f"{html}"
    if "password" in html:
        print(f"found password: {second_page}")

def loop(next_page):
    global a
    driver.get(next_page)
    res2=driver.find_elements(By.CLASS_NAME,"")#class name in html of tag
    for a in res2:
        pass
        #print(a.text)
        if "py" in a.text:
            second_page =f"{next_page}/{a.text}"
            print(second_page)
        elif "js" in a.text:
            second_page=f"{next_page}/{a.text}"
        print(second_page)
    

for i in res:
    links.append(i.text)
    print(links)
for l in links:
    next_page =f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)
    #print(flink)
driver.quit()


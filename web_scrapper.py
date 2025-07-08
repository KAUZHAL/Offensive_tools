import requests
from bs4 import BeautifulSoup
HEADERS={"User-Agent":"Mozilla/5.0(X11;Linux x86_84) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
""" Option 1 
def scrape_github_repos(username):
    url=f"https://github.com/{username}?tab=repositories"
    response=requests.get(url,headers=HEADERS)
    if response.status_code !=200:
        print(f"Failed to fwetch data.Status code:{response.status_code}")
        return []
    soup=BeautifulSoup(response.text,'html.parser')
    repos=soup.find_all('div',class_='wb-break-all')
    repo_names=[]
    for repo in repos:
        repo_name=repo.a.text.strip()
        repo_names.append(repo_name)
    return repo_names
"""
#Option 2
def get_repos_via_api(username,token):
    url=f"https://api.github.com/users/{username}/repos"
    headers={"Authorization":f"token{token}"}
    reponse=requests.get(url,headers=headers)
    return response.json()
if __name__=="__main__":
    username=input("Enter the GitHub username to scrape:")
    repos=scrape_github_repos(username)
    if repos:
        print(f"Repositories of {username}:")
        for i,repo in enumerate(repos,1):
            print(f"{i}.{repo}")
    else:
        print("No repositories found or failed to scrape")
#Option 3 using Chrome Browser webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
on = True
while on:
    def five_seconds():
        time.sleep(5)
        driver.get("https://www.google.com") #or anyother e-commerce-website or github link
        price =driver.find_element(By.CLASS_NAME," ")#class name in double quotes of html
        print(price.text)
        driver.quit()
    five_seconds()



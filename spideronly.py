"""https://en.wikipedia.org/wiki/Programmer
import requests
from bs4 import BeautifulSoup
def get_page(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    tag=soup.find_all("a")#finds all the anchor tags
    #print(soup.find(id="mw-searchButton"))
    #print(soup.title.string)
    for t in tag:
        url2=t.get("href")
        print(url2)
get_page(input("Enter the URL to scrape: "))"""

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *
import subprocess
visited_urls=set()
def spider_urls(url,keyword,output_file):
    try:
        response=requests.get(url)
    except Exception as e:
        print(f"Request failed for {url}:{e}")
        return
    if response.status_code == 200:
        soup=BeautifulSoup(response.content,'html.parser')
        a_tag =soup.find_all('a')
        urls=[]
        for tag in a_tag:
            href=tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        #print(urls)
        for i in urls:
            if i not in visited_urls:
                visited_urls.add(i)
                url_join=urljoin(url,i)
                if keyword in url_join:
                    print(url_join)
                    with open(output_file,"a") as file:
                        file.write(url_join + "\n")
                    spider_urls(url_join,keyword,output_file)
            else:
                pass   
url=input("Enter the URL to scrape: ")
keyword=input("Enter the keyword to search: ")
output_file="output_urls.txt"
spider_urls(url,keyword,output_file)
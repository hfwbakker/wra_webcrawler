# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver import Firefox 

import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome(ChromeDriverManager().install())

# search_url = "https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568" 
search_url = "https://www.wolframalpha.com/input/?i={q}"

driver.get(search_url.format(q='www.teamliquid.net'))

#Scroll to the end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(15)#sleep_between_interactions

#Locate the images to be scraped from the current page 
imgResults = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
totalResults = len(imgResults)

search_results = driver.find_elements_by_xpath("//img[contains(@class, '_3vyrn')]")

print("\n\nPRINTING SEARCH RESULTS \n\n")
print(search_results)

# driver = webdriver.Firefox()
# driver.get('https://www.wolframalpha.com/input/?i=www.teamliquid.net')

# print("Hello world")

# target_urls = ['https://lady.gmw.cn/2021-04/25/content_34793576.htm', 'http://beauty.rayli.com.cn/news/2021-04-30/693829.shtml', 'http://news.china-ef.com/677100.html']

# html_text = requests.get('https://www.wolframalpha.com/input/?i=www.teamliquid.net').text
# soup = BeautifulSoup(html_text, 'lxml')
# try:
#     text_content = soup.find('img').get('alt')
#     print(text_content)
# except:
#     print("Nope")
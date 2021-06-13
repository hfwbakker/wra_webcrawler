import os.path
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import pyperclip
import re
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

###########################################################################
### SECTION 1: SCRAPING THE DATA AND PUTTING IT INTO A PANDAS DATAFRAME ###
###########################################################################

# pandas logic
data = {'url':[], 'domain':[], 'host':[], 'name':[], 'daily_page_views':[], 'daily_visitors':[], 'site_rank':[]}
df = pd.DataFrame(data)

# scraping logic
def get_wra_info():
    time.sleep(15)
    
    search_results = driver.find_elements_by_xpath("//img[@class='_3vyrn']")
    print("printing search results")
    print(search_results)
    print("Search result length:")
    print(len(search_results))
    domain_data         = "N/A"
    host_data           = "N/A"
    name_data           = "N/A"
    daily_page_views    = "N/A"
    daily_visitors      = "N/A"
    site_rank           = "N/A"

    for i in search_results:
        if "(domain)" in i.get_attribute('alt'):
            domain_data = i.get_attribute('alt')
        if "name |" in i.get_attribute('alt'):
            name_data = i.get_attribute('alt')
        if "daily page views |" in i.get_attribute('alt'):
            stats_data = i.get_attribute('alt').splitlines()

            daily_page_views    = int(re.findall(r'\d+', stats_data[0])[0])
            if 'million' in stats_data[0]:
                daily_page_views = int(daily_page_views) * 1000000
            if 'billion' in stats_data[0]:
                daily_page_views = int(daily_page_views) * 1000000000
            
            daily_visitors      = int(re.findall(r'\d+', stats_data[1])[0])
            if 'million' in stats_data[1]:
                daily_visitors = int(daily_visitors) * 1000000
            if 'billion' in stats_data[1]:
                daily_visitors = int(daily_visitors) * 1000000000
            
            site_rank           = int(re.findall(r'\d+', stats_data[2])[0])
            
        
    new_row = {'url':"URL", 
               'domain': domain_data, 
               'host':host_data, 'name':name_data, 
               'daily_page_views': daily_page_views, 
               'daily_visitors': daily_visitors, 
               'site_rank': site_rank}

    count = 1
    for i in search_results:
        print(f"result {count} = {i.get_attribute('alt')}")
        count += 1
        
    return new_row

# initialize and install / check webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# url_list = ["https://lady.gmw.cn/2021-04/25/content_34793576.htm", "www.teamliquid.net"]
url_list = pyperclip.paste().split()
print(url_list)

wra_url = "https://www.wolframalpha.com/input/?i={q}"

### MAIN FUNCTION LOOP ###
for i in range(len(url_list)):
    print("Getting results for:")
    print(url_list[i])
    driver.get(wra_url.format(q=url_list[i]))
    df = df.append(get_wra_info(), ignore_index=True)
    print("\n\n")

print(df)
driver.quit()

##########################################################
### SECTION 2: EDITING, FORMATTING, OUTPUTTING DF DATA ###
##########################################################

wb = openpyxl.Workbook()
ws = wb.active

for r in dataframe_to_rows(df, index=True):
	ws.append(r)

ws.column_dimensions["B"].width = 5
ws.column_dimensions["C"].width = 20
ws.column_dimensions["D"].width = 10
ws.column_dimensions["E"].width = 100
ws.column_dimensions["F"].width = 15
ws.column_dimensions["G"].width = 15
ws.column_dimensions["H"].width = 10

filecount = 0
while os.path.isfile(f"output/output{filecount}.xlsx") == True:
    filecount += 1
wb.save(f"output/output{filecount}.xlsx")
print(f"Saved to 'output/output{filecount}.xlsx")

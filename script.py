import os
import os.path
import selenium
from selenium import webdriver
import time
# from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import pyperclip

###########################################################################
### SECTION 1: SCRAPING THE DATA AND PUTTING IT INTO A PANDAS DATAFRAME ###
###########################################################################

# pandas logic
data = {'url':[], 'domain':[], 'host':[], 'name':[], 'stats':[]}
df = pd.DataFrame(data)

# scraping logic
def get_wra_info():
    time.sleep(15)
    
    search_results = driver.find_elements_by_xpath("//img[@class='_3vyrn']")
    print("printing search results")
    print(search_results)
    print("Search result length:")
    print(len(search_results))
    domain_data = "N/A"
    host_data = "N/A"
    name_data = "N/A"
    stats_data = "N/A"

    for i in search_results:
        if "(domain)" in i.get_attribute('alt'):
            domain_data = i.get_attribute('alt')
        if "name |" in i.get_attribute('alt'):
            name_data = i.get_attribute('alt')
        if "daily page views |" in i.get_attribute('alt'):
            stats_data = i.get_attribute('alt')
            
        
    new_row = {'url':"URL", 'domain': domain_data, 'host':host_data, 'name':name_data, 'stats':stats_data}

    count = 1
    for i in search_results:
        print(f"result {count} = {i.get_attribute('alt')}")
        count += 1
        
    return new_row

    # except:
    #     print("ERROR: Something caused an error. Reasons: WRA does not have info on this URL, or the page is taking too long to load.")
    #     new_row = {'url':"N/A", 'domain': "N/A", 'host':"N/A", 'name':"N/A", 'stats':"N/A"}

    #     return new_row

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

# output files, while ensuring to not remove existing output files.
filecount = 0
while os.path.isfile(f"ouput/output{filecount}.xlsx") == True:
    filecount += 1
df.to_excel(f"output/output{filecount}.xlsx")
print(f"Output to 'output/output{filecount}.xlsx'")

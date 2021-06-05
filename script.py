import os
import selenium
from selenium import webdriver
import time
# from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd

###########################################################################
### SECTION 1: SCRAPING THE DATA AND PUTTING IT INTO A PANDAS DATAFRAME ###
###########################################################################

# pandas logic
data = {'url':[], 'domain':[], 'host':[], 'name':[], 'stats':[]}
df = pd.DataFrame(data)

# df = df.append(new_row, ignore_index=True)

# scraping logic
def get_wra_info():
    time.sleep(15)
    
    try:
        search_results = driver.find_elements_by_xpath("//img[@class='_3vyrn']")
        print("printing search results")
        print(search_results)
        print("Search result length:")
        print(len(search_results))

        new_row = {'url':"URL", 'domain':search_results[0].get_attribute('alt'), 'host':search_results[1].get_attribute('alt'), 'name':search_results[2].get_attribute('alt'), 'stats':search_results[3].get_attribute('alt')}

        count = 1
        for i in search_results:
            print(f"result {count} = {i.get_attribute('alt')}")
            count += 1
    
        return new_row

    except:
        print("ERROR: Something caused an error. Perhaps your internet is loading too slowly? Increase sleep time and try again.")
        driver.quit()
        exit(0)

# initialize and install / check webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

url_list = ["https://lady.gmw.cn/2021-04/25/content_34793576.htm", "www.teamliquid.net"]

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
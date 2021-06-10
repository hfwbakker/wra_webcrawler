PROJECT:
- Create a webcrawler that gets specific information on a series of website from wolframalpha.com (WRA), and output them to an excel sheet.
- Possible challenges: website outputs info in .img, presumably to hinder webcrawlers.
- Tools: beautifulsoup, pandas, requests, selenium, geckodriver (consider openpyxl, os.path, pprint)
- Project steps breakdown:
    1) write code to enter a search term on the WRA website and then navigate there. (e.g. 'https://www.wolframalpha.com/input/?i=' + search_url)
    2) write code to fetch or read the relevant data.
    3) write code filter and save that data (e.g. a pandas dataframe).
    4) write code to automate reading urls from client .xlsx file (e.g. websites to check) and fetch and save that data.
    5) Output in relevant format to .xlsx file.


NEXT UP:
- Look at "excel_it" function in projects/python_webscraper/scraper_scripts/axios_scraper.py and create a similar function to neatly output pandas data into an excel sheet.
- Is it possible to create some script that user can just double click that will automatically input the right commands into terminal? Like a Bash script? -> I think its called a shell script.
- Clean up code.


LOG:
--- Thursday, June 10th, 2021 ---
- Reinstalled all dependencies after having to completely reset (and repair) computer.
- Created test_develop.py for creating code snippets to be implemented in to the main script. The current contents take in a long multiline string and uses regex to take out the numbers relevant to client.
- Regex now takes out the number values out of the stats data and splits them into different columns, BUT as it turns out, numbers are combined with strings: e.g. not 420,000 but 420 thousand. Should adjust regex to take out this value as a whole. Then add another column that "translates" these strings in to usable ints/floats.
- Values written as a string now correctly get translated to a number. '240 million' becomes 240,000,000.

--- Sunday, June 6th, 2021 ---
- Script outputs info to excel sheet.
- Through using pyperclip the user can now copy a list of URL's from an excel file and the script will automatically read them from clipboard.
- Script now (mostly) correctly finds which info belongs in which column, and inputs "N/A" if data is missing.

--- Saturday, June 5th, 2021 ---
- Script now fetches relevant data from WRA page.
- Implemented a for loop that loops through a list of URLs and grabs the relevant info.
- Selenium sorta makes sense now.
- Script now accurately puts data into pandas dataframe.

--- Monday, May 31st, 2021 ---
- More research on Selenium, no actual coding.

--- Sunday, May 30th, 2021 ---
- WRA does not work without JavaScript because it generates some data presumably. This means that a purely html parser such as beautifulsoup won't do the trick. Added selenium and chromedriver-binary to emulate running a page.
- More or less managed to get a chrome window opened with selenium and managed to select an item although it returns gibberish.

--- Saturday, May 29th, 2021 ---
- Updated POA
- Created virtual environment with python 3.9, beautifulsoup, requests, and pandas.

--- Friday, May 28th, 2021 ---
- Created README, repository
- Wrote intial POA, defined goals
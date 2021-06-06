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
- Regex so the number of visitors automatically becomes a useable number in output excel sheet instead of a string
- Final column "stats" now has long strings like "daily page views | ≈ 51000 hits/d (hits per day)... etc" -> this should be split up in seperate colums "daily page views", "daily visitors", "site rank", "domain online". All columns should contain direclty usuable numbers, not strings. Excess words (like descriptions) to be filtered out.
- Is it possible to create some script that user can just double click that will automatically input the right commands into terminal? Like a Bash script?


LOG:
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
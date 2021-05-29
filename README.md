PROJECT:
- Create a webcrawler that gets specific information on a series of website from wolframalpha.com (WRA), and output them to an excel sheet.
- Possible challenges: website outputs info in .img, presumably to hinder webcrawlers.
- Tools: beautifulsoup, pandas, requests (consider openpyxl, os.path, pprint)


NEXT UP:
- Get more details about project parameters.
- Figure out tech deck.
- Figure out of Python requests can handle working with search requests inside a website that no doubt has it's tools to hinder webcrawlers.
- Project steps breakdown:
    1) write code to enter a search term on the WRA website and then navigate there.
    2) write code to fetch or read the relevant data.
    3) write code filter and save that data (e.g. a pandas dataframe).
    4) write code to automate reading urls from client .xlsx file (e.g. websites to check) and fetch and save that data.
    5) Output in relevant format to .xlsx file.


LOG:
--- Saturday, May 29th, 2021 ---
- Updated POA
- Created virtual environment with python 3.9, beautifulsoup, requests, and pandas.

--- Friday, May 28th, 2021 ---
- Created README, repository
- Wrote intial POA, defined goals
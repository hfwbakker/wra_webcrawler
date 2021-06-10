import re

#input string
string = """
daily page views | ≈ 42000 hits/d (hits per day) (based on Alexa estimates, as of 2021-06-10)
daily visitors | ≈ 21000 visits/d (visits per day) (based on Alexa estimates, as of 2021-06-10)
site rank | ≈ 156138th
domain online | 2002-09-24 (≈19 years ago)
(based on Alexa estimates, as of 2021-06-10, and assuming 4.209 billion global internet users)
"""

#split string into a list of items and remove empty ones
split_string = string.splitlines()
del split_string[0]
del split_string[-1]

# for i in split_string:
#     print(i)

# re.findall(r'\d+', 'hello 42 I\'m a 32 string 30')


# assigns split list values to individual values.
# large numbers are written as e.g. 240 million (a string)
# update regex to take out these strings as a whole, and then translate them to a usable number.
# example code:
# e.g. string_outtake = 240 million; string_outtake_num = re.find(num, string_outtake (= 240)) if string_outtake.contains('million'); number * 1,000,000.
daily_page_views    = re.findall(r'\d+', split_string[0])[0] # -> daily page views | ≈ 42000 hits/d (hits per day) (based on Alexa estimates, as of 2021-06-10)
daily_visitors      = re.findall(r'\d+', split_string[1])[0] # -> daily visitors | ≈ 21000 visits/d (visits per day) (based on Alexa estimates, as of 2021-06-10)
site_rank           = re.findall(r'\d+', split_string[2])[0] # -> site rank | ≈ 156138th

print(daily_page_views)
print(daily_visitors)
print(site_rank)
# https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions

from importlib.metadata import distribution
import mechanicalsoup
import pandas as pd
import sqlite3

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

# extract table headers 
th = browser.page.find_all("th", attrs={"class": "table-rh"})
distribution_ = [value.text.replace("\n", "") for value in th]
distribution_ = distribution_[:98]
for i in distribution_:
    print(i)

# print(distribution_.index("Zorin OS"))

# extract table data elements
td = browser.page.find_all("td")
columns = [value.text.replace("\n", "") for value in td]

# print(columns.index("AlmaLinux Foundation"))
# print(columns.index("Binary blobs"))

columns = columns[6:1084]
print(columns)

# extract sort headers
thh = browser.page.find_all("th")
headers = [value.text.replace("\n", "") for value in thh]
headers = headers[1:11]
print(headers)

dictionary = {"Distribution": distribution_}

for idx, key in enumerate(headers):
    dictionary[key] = columns[idx:][::11]


df = pd.DataFrame(data = dictionary)
print(df.head(10))
print(df.tail(10))



# print(distribution__.index("Founder"))
# print(distribution__.index("Status"))








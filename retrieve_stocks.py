import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
headers = {'User-Agent': 'StockListBot/1.0 (https://github.com/monil-p; Mr.Moe582@gmail.com)'}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.content, "html.parser")

table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="constituents")


headers = []


table_tbody = table.find("tbody")

table_trs = table_tbody.find_all('tr')

data = []

for table_tr in table_trs:
    table_tds = table_tr.find_all('td')
    table_ths = table_tr.find_all('th')

    for th in table_ths:
        row = th.get_text(strip=True)

        headers.append(row)

    
    row = [td.get_text(strip=True) for td in table_tds]        

    data.append(row)

df = pd.DataFrame(data, columns=headers)

df.to_csv("sp500_companies.csv", index=False)

print("Exported to sp500_companies.csv")

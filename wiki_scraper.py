from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_most_valuable_companies_in_India"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

# years
year18 = soup.find('span',{'id':'2018'}).text
year16_17 = soup.find('span',{'id':'2016-17'}).text
year17_18 = soup.find('span',{'id':'2017-18'}).text

# all tables
my_tables = soup.select("table.wikitable")

# returns dataframe 
def wiki_tab(name):
    rows = name.find_all('tr')
    columns = [x.text.replace('\n', '') for x in rows[0].find_all('th')]
    df1 = pd.DataFrame(columns = columns)
    for i in range(1, len(rows)):
        tds = rows[i].find_all('td')
        values = [td.text.replace('\n', '') for td in tds]
        df1 = df1.append(pd.Series(values, index = columns),ignore_index=True)
    return df1

# first_table
table1 = my_tables[0]
wiki_tab(table1)


df = wiki_tab(table1)
print(df)
# saving it as csv
df.to_csv(r'C:\Users\Lenovo\Desktop\MAIN\Project_Work\Beautiful_Soup\\'+ 'top10.csv', index=False)
# in a dictionary
data = df.to_dict()

# second_table
table2 = my_tables[1]
df = wiki_tab(table2)
print(df)

# third_table
table3 = my_tables[2]
df = wiki_tab(table3)
print(df)
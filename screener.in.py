from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Referer' : 'https://www.screener.in/login/'
}

# LOGIN - Not required for scraping below content
s0 = requests.session()
screener_url1 = 'https://www.screener.in/login/'
r1 = s0.get(screener_url1, headers = headers)  # get request for login page 
soup1 = BeautifulSoup(r1.content, 'lxml')
csrf = soup1.find('input', {"name" : "csrfmiddlewaretoken"})
csrf_token = csrf['value']  #CSRFmiddlewareToken from HTML  

# Enter your username and password   
login_data = dict(csrfmiddlewaretoken=csrf_token, next='/', username='username', password='password')
r2 = s0.post(screener_url1, data = login_data, headers = headers) # post request for login 
# LOGIN COMPLETE

# One can skip login and start from here
# STOCK PAGE
url = "https://www.screener.in/company/RELIANCE/consolidated/"
stock_page = requests.get(url)
soup = BeautifulSoup(stock_page.content, 'lxml')

# ALTERNATE EASY WAY FOR SCRAPING TABLES
df = pd.read_html(url)

# QUARTERLY RESULTS
quarter_res = df[0].to_dict()
# PROFIT-LOSS STATEMENTS
pl_stats = df[1].to_dict()
# COMPOUND SALES GROWTH
cmp_sales_growth = df[2].to_dict()   
# COMPOUND PROFIT GROWTH
cmp_profit_growth = df[3].to_dict()
# STOCK PRICE CAGR
cagr = df[4].to_dict()
# RETURN ON EQUITY
roe = df[5].to_dict()
# BALANCESHEETS
bal_sheets = df[6].to_dict()
# CASHFLOW
cashf_stats = df[7].to_dict()

# ANOTHER WAY FOR SCRAPING TABLE
# SELECTING ALL TABLES
my_tables = soup.select("table.data-table")

# EXTRACTING TABLE 1 BY 1 USING PANDAS
# QUARTERLY RESULTS
table1 = my_tables[0]
rows = table1.find_all('tr')
columns = [x.text.replace('\n', '').strip() for x in rows[0].find_all('th')]
df1 = pd.DataFrame(columns = columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n', '').strip() for td in tds]
    df1 = df1.append(pd.Series(values, index = columns),ignore_index=True)
# quarterly_results = df1.to_string(index=False)
quarterly_results = df1.to_dict() 

# BALANCE SHEETS
table1 = my_tables[2]
rows = table1.find_all('tr')
columns = [x.text.replace('\n', '').strip() for x in rows[0].find_all('th')]
df2 = pd.DataFrame(columns = columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n', '').strip() for td in tds]
    df2 = df2.append(pd.Series(values, index = columns),ignore_index=True)
balance_sheets = df2.to_dict() 

# CASHFLOW STATEMENTS
table1 = my_tables[3]
rows = table1.find_all('tr')
columns = [x.text.replace('\n', '').strip() for x in rows[0].find_all('th')]
df3 = pd.DataFrame(columns = columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n', '').strip() for td in tds]
    df3 = df3.append(pd.Series(values, index = columns),ignore_index=True)
cashflow_statements = df3.to_dict() 

# FOR PROFIT-LOSS STATEMENT
theaders = my_tables[1].select("th")
trowlabels = my_tables[1].select("section#profit-loss td.text")
lst1 = my_tables[1].select("section#profit-loss table.data-table td:nth-of-type(2)")
lst2 = my_tables[1].select("section#profit-loss td:nth-of-type(3)")
lst3 = my_tables[1].select("section#profit-loss td:nth-of-type(4)")
lst4 = my_tables[1].select("section#profit-loss td:nth-of-type(5)")
lst5 = my_tables[1].select("section#profit-loss td:nth-of-type(6)")
lst6 = my_tables[1].select("section#profit-loss td:nth-of-type(7)")
lst7 = my_tables[1].select("section#profit-loss td:nth-of-type(8)")
lst8 = my_tables[1].select("section#profit-loss td:nth-of-type(9)")
lst9 = my_tables[1].select("section#profit-loss td:nth-of-type(10)")
lst10 = my_tables[1].select("section#profit-loss td:nth-of-type(11)")
lst11 = my_tables[1].select("section#profit-loss td:nth-of-type(12)")
lst12 = my_tables[1].select("section#profit-loss td:nth-of-type(13)")
# FOR COLUMN LABELS  
theaders_data = list()
for i in range(1,13): 
    data = theaders[i].text
    theaders_data.append(data)
# FOR ROW LABELS
trowlabels_data = list()
for i in range(0,12): 
    data = trowlabels[i].text.strip()
    trowlabels_data.append(data)

# DEFINED FOR PROFIT0LOSS STATEMENT DESIGN
lst1_data, lst2_data, lst3_data, lst4_data, lst5_data, lst6_data = list(), list(), list(), list(), list(), list()
lst7_data, lst8_data, lst9_data, lst10_data, lst11_data, lst12_data =  list(), list(), list(), list(), list(), list()
# FOR ROW DATA
for i in range(0,12):
    data1 = lst1[i].text
    lst1_data.append(data1)
    data2 = lst2[i].text
    lst2_data.append(data2)
    data3 = lst3[i].text
    lst3_data.append(data3)
    data4 = lst4[i].text
    lst4_data.append(data4)
    data5 = lst5[i].text
    lst5_data.append(data5)
    data6 = lst6[i].text
    lst6_data.append(data6)
    data7 = lst7[i].text
    lst7_data.append(data7)
    data8 = lst8[i].text
    lst8_data.append(data8)
    data9 = lst9[i].text
    lst9_data.append(data9)
    data10 = lst10[i].text
    lst10_data.append(data10)
    data11 = lst11[i].text
    lst11_data.append(data11)
    data12 = lst12[i].text
    lst12_data.append(data12)

# CREATING DF WITH PANDAS 
data = {
    'Quote': trowlabels_data,
    theaders_data[0] : lst1_data,
    theaders_data[1] : lst2_data,
    theaders_data[2] : lst3_data,
    theaders_data[3] : lst4_data,
    theaders_data[4] : lst5_data,
    theaders_data[5] : lst6_data,
    theaders_data[6] : lst7_data,
    theaders_data[7] : lst8_data,
    theaders_data[8] : lst9_data,
    theaders_data[9] : lst10_data,
    theaders_data[10] : lst11_data,
    theaders_data[11] : lst12_data,
}
df5 = pd.DataFrame(data)
pl_statements = df5.to_dict() 

# ROE TABLE
data, data1, roe_tab_trs, roe_tab_tds = list(), list(), list(), list()
roe_tab_th = soup.select("table.three:nth-of-type(4) th")[0].text
roe_tab_tr = soup.select("table.three:nth-of-type(4) td:nth-of-type(1)")
roe_tab_td = soup.select("table.three:nth-of-type(4) td:nth-of-type(2)")
for i in range(4):
    data = roe_tab_tr[i].text
    roe_tab_trs.append(data)
    data1 = roe_tab_td[i].text
    roe_tab_tds.append(data1)
roe_table = dict(zip(roe_tab_trs,roe_tab_tds))

# COMPOUND SALES GROWTH TABLE
data, data1, cmp_sale_trs, cmp_sale_tds = list(), list(), list(), list()
cmp_sale_th = soup.select("table.three:nth-of-type(1) th")[0].text
cmp_sale_tr = soup.select("table.three:nth-of-type(1) td:nth-of-type(1)")
cmp_sale_td = soup.select("table.three:nth-of-type(1) td:nth-of-type(2)")
for i in range(4):
    data = cmp_sale_tr[i].text
    cmp_sale_trs.append(data)
    data1 = cmp_sale_td[i].text
    cmp_sale_tds.append(data1)
csg_table = dict(zip(cmp_sale_trs,cmp_sale_tds))

# COMPOUND PROFIT GROWTH TABLE
data, data1, cmp_pro_trs, cmp_pro_tds = list(), list(), list(), list()
cmp_pro_th = soup.select("table.three:nth-of-type(2) th")[0].text
cmp_pro_tr = soup.select("table.three:nth-of-type(2) td:nth-of-type(1)")
cmp_pro_td = soup.select("table.three:nth-of-type(2) td:nth-of-type(2)")
for i in range(4):
    data = cmp_pro_tr[i].text
    cmp_pro_trs.append(data)
    data1 = cmp_pro_td[i].text
    cmp_pro_tds.append(data1)
cpg_table = dict(zip(cmp_pro_trs,cmp_pro_tds))

#  STOCK PRICE CAGR
data, data1, cagr_trs, cagr_tds = list(), list(), list(), list()
cagr_th = soup.select("table.three:nth-of-type(2) th")[0].text
cagr_tr = soup.select("table.three:nth-of-type(2) td:nth-of-type(1)")
cagr_td = soup.select("table.three:nth-of-type(2) td:nth-of-type(2)")
for i in range(4):
    data = cagr_tr[i].text
    cagr_trs.append(data)
    data1 = cagr_td[i].text
    cagr_tds.append(data1)
cagr_table = dict(zip(cagr_trs,cagr_tds))

# RATIOS OF ROCE, DEBTOR_DAYS AND INVENTORY_TURNOVER
# Cash-flow
table1 = my_tables[4]
rows = table1.find_all('tr')
columns = [x.text.replace('\n', '').strip() for x in rows[0].find_all('th')]
df4 = pd.DataFrame(columns = columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n', '').strip() for td in tds]
    df4 = df4.append(pd.Series(values, index = columns),ignore_index=True)
ratio_statements = df4.to_dict() 

# PROS AND CONS 
# EXTRACTING TEXT_DATA FROM TAGS
pros, cons = list(), list()
con = soup.select("div.warning")
pro = soup.select("div.success")
for tag in con:
    cons = tag.text.strip().replace('Cons:','').replace('\n',' ')
for tag in pro:
    pros = tag.text.strip().replace('\n',' ').replace('Pros:','')
pros_cons = {'pros' : pros, 'cons' : cons}

# ANNUAL REPORT LINKS
link_text, links, data, data_text = list(), list(), list(), list()
for j in range(1,6):
    for link in soup.select("div.three:nth-of-type(2) li:nth-of-type("+str(j)+") a"):
        data = (link['href'])
        links.append(data)
        data_text = link.text.strip().replace("\n","")
        link_text.append(data_text)
annual_reports =  dict(zip(link_text, links))

# CREDIT RATINGSannual_
link_text, links, data, data_text, count = list(), list(), list(), list(), int()
count = len(soup.select("div.three:nth-of-type(3) a"))
for j in range(1,count+1):
    for link in soup.select("div.three:nth-of-type(3) li:nth-of-type("+str(j)+") a"):
        data = (link['href'])
        links.append(data)
        data_text = link.text.strip().replace("\n","")
        link_text.append(data_text)
credit_ratings = dict(zip(link_text, links))


# EXTRACTING LINKS
web_link = dict()
for link in soup.select("li.four:nth-of-type(10) a:nth-of-type(1)"):
    web_link['bse_link'] = (link['href'])
for link in soup.select("li.four:nth-of-type(10) a:nth-of-type(2)"):
    web_link['nse_link'] = (link['href'])
for link in soup.select("li.four:nth-of-type(11) a"):
    web_link['comp_link'] = (link['href'])
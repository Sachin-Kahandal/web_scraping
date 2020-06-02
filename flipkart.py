import requests
from bs4 import BeautifulSoup


url = 'https://www.flipkart.com/mobiles/pr?filterNone=true&sid=tyy%2C4io&p%5B%5D=sort%3Dpopularity&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_5_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_0244AFBL8QS6_wp3&fm=neo%2Fmerchandising&iid=M_7d9210b8-1491-4c68-9c68-c7e90a6a9829_5.0244AFBL8QS6&ppt=clp&ppn=mobile-phones-store&ssid=5gt6b71ztc0000001589278269024'
res = requests.get(url)
coup = BeautifulSoup(res.text, 'lxml')

page = coup.select('div._2zg3yZ > span:nth-of-type(1)')[0].text
try:
    max_page_no = page.split('Page 1 of')[1].strip()
except IndexError:
    max_page_no = 1

k = 0
for i in range(1, int(max_page_no)+1):
    url1 = 'https://www.flipkart.com/mobiles/pr?filterNone=true&sid=tyy%2C4io&p%5B%5D=sort%3Dpopularity&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_5_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_0244AFBL8QS6_wp3&fm=neo%2Fmerchandising&iid=M_7d9210b8-1491-4c68-9c68-c7e90a6a9829_5.0244AFBL8QS6&ppt=clp&ppn=mobile-phones-store&ssid=5gt6b71ztc0000001589278269024&page='+str(i)
    res1 = requests.get(url1)
    soup = BeautifulSoup(res1.text,'lxml')
    k = k+1
    count = len(soup.select('div._3wU53n'))
    o = 0
    for j in range(2,count+2):
        try:
            field = soup.select('div.bhgxx2:nth-of-type('+str(j)+') div._1UoZlX')[0]
        except:
            msg = {'Info':'page no '+str(k)+' is empty'}
            print(msg)
        o = o + 1
        mobile = dict()
        mobile['page_no'] = k
        mobile['item_no'] = o
        mobile['name'] = field.select("div._3wU53n")[0].text
        mobile['price'] = field.select("div._1vC4OE")[0].text
        mobile['features'] = field.select('ul.vFw0gD')[0].text
        try:
            mobile['ratings'] = field.select('span div.hGSR34')[0].text
        except IndexError:
            mobile['ratings'] = 'Not available'
        print(mobile)
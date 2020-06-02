import requests
from bs4 import BeautifulSoup
import smtplib
from twilio.rest import Client


url = 'https://www.croma.com/apple-iphone-8-plus-gold-64-gb-3-gb-ram-/p/205737'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

def price_check():
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    price = int(soup.select("span.pdpPrice")[0].text[1:7].replace(",",""))
    best_buy = 36000
    if price < best_buy:
        send_mail()
        # send_text()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # ehlo is SMTP command sent by email server to identify itself when connecting to another email server
    server.ehlo()
    # starttls encrypts the connection
    server.starttls()
    server.ehlo()

    # you got to set app password for this
    # Google Account -> Security -> App password -> Generate
    # use that generated passwoed below
    sender = 'email_id'
    password = 'pass'
    # Here you are sending mail  to yourself
    # You can add multiple email address using list
    reciever = sender

    server.login(sender, password)
     
    subject = 'Drop in price of iphone 8+ !!! yay'
    body = ' Here is the link \n https://www.croma.com/apple-iphone-8-plus-gold-64-gb-3-gb-ram-/p/205737'

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(sender, reciever, msg)
    server.quit()
    print("Mail Sent")

def send_text():
    # Register an free account for first time on twilio 
    # select phone -> text message and generate auth_token will generate
    # free account allows only upto 10 text
    account_sid = 'acc_id'
    auth_token = 'auth_token'
    client = Client(account_sid, auth_token)

    subject = 'Drop in price of iphone 8+ !!! yay'
    body = 'Here is the link https://www.croma.com/apple-iphone-8-plus-gold-64-gb-3-gb-ram-/p/205737'

    message = client.messages.create(
            body= f"Subject: {subject}\n\n{body}"
            )    

price_check()
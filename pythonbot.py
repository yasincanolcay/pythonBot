#import libraries

import telegram.ext
import time
import os
import telegram
import datetime
import requests

timeDate = time.strftime('%d:%m:%Y:%H:%M:%S')

with open('token.txt','r') as f:

    TOKEN = f.read()



def resim1(update,source):
    update.message.reply_text('Lütfen bekleyiniz...')
    resim1 = open('assets/images/resim1.jpg','rb')
    time.sleep(3)
    update.message.reply_photo(resim1)


def resim2(update,source):
    update.message.reply_text('Lütfen bekleyiniz...')
    resim2 = open('assets/images/resim2.jpg','rb')
    time.sleep(3)
    update.message.reply_photo(resim2)


def resim3(update,source):
    update.message.reply_text('Lütfen bekleyiniz...')
    resim3 = open('assets/images/resim3.jpg','rb')
    time.sleep(3)
    update.message.reply_photo(resim3)



def resim4(update,source):
    update.message.reply_text('Lütfen bekleyiniz...')
    resim4 = open('assets/images/resim4.jpg','rb')
    time.sleep(3)
    update.message.reply_photo(resim4)

  
    
    
def hello(update,source):
    update.message.reply_text('Merhaba nasılsınız.')
    

def havaDurumu(update, source):

    resim = "http://openweathermap.org/img/wn/{}@2x.png"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=".format('izmir')
    api = "e7d2c6c38b9ae7616ec4a3579c9313cf&lang=tr"
    ara = url+api
    r = requests.get(ara)
    yaz = r.json()
    isim = yaz["name"]
    country = yaz["sys"]["country"]
    temp = int(yaz["main"]["temp"]-273.15)
    con = yaz["weather"][0]["description"]
    tarih = datetime.datetime.now()
    mesg = "{} ülkesi {} şehiri hava durumu\nsıcaklık:{}ϲ∘\ndurum:{}\nTarih: {}".format(country,isim,temp,con,tarih)
    time.sleep(3)
    update.message.reply_text(mesg)



update = telegram.ext.Updater(TOKEN,use_context=True)
disp = update.dispatcher

disp.add_handler(telegram.ext.CommandHandler('resim1',resim1))
disp.add_handler(telegram.ext.CommandHandler('resim2',resim2))
disp.add_handler(telegram.ext.CommandHandler('resim3',resim3))
disp.add_handler(telegram.ext.CommandHandler('resim4',resim4))
disp.add_handler(telegram.ext.CommandHandler('merhaba',hello))
disp.add_handler(telegram.ext.CommandHandler('havadurumu',havaDurumu))


update.start_polling()
update.idle()
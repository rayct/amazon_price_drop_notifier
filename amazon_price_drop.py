import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

while True:
    current_time=time.strftime("%H:%M:%S")
    r = requests.get("")
    c = r.content
    toast = ToastNotifier()
    soup = BeautifulSoup(c, "html.parser")
    try:
        try:
            price = soup.find('span', {'id': 'priceblock_ourprice'})
            price = price.text.split()
            price = price[1]
            price = price.replace(",", "")
            price.show_toast("Product Notification", "Product is avilable at Regular Price")

        except:
            price = soup.find('span', {'id': 'priceblock_dealprice'})
            price = price.text.split()
            price = price[1]
            price = price.replace(",", "")
            price.show_toast("Product Notification", "Product is avilable at Exclusive Offer Price")

    except:
        price_type = "Product Not Available"
    print(price_type)
    time.sleep(10)

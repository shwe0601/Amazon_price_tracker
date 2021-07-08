import requests
import lxml
import smtplib
from bs4 import BeautifulSoup


BUY_PRICE=200000

URL = "https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T31M6/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12+pro+max&qid=1625735626&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR01QMFJIM0g2NFlMJmVuY3J5cHRlZElkPUEwOTY0NDUxMjZDUzdTRzBMTVNEWCZlbmNyeXB0ZWRBZElkPUEwMjY3MTgxM0hET0RaNTlXRDZJRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(id="priceblock_ourprice").get_text()
price_without_symbol = price.split("₹")[1].replace(",", "")
new_price=float(price_without_symbol)

title = soup.find(id="productTitle").get_text().strip()

if new_price<BUY_PRICE:
    message=f"{title} is now {new_price} BUY SOON"


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result=connection.login(user="hannaajen@gmail.com",password="shweta0601")
        connection.sendmail(
            from_addr="hannaajen@gmail.com",
            to_addrs="shwetabadrinarayanan@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )




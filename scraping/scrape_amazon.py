import requests #download website
from bs4 import BeautifulSoup #Extract product data
import pandas as pd #Store data in table
import time #Delay scraping
from datetime import datetime #Store date

#Program stores website link.
BASE_URL = "https://www.amazon.in/s?k=laptops&page={}"

#Prevents blocking.
HEADERS = {
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
" (KHTML, like Gecko) Chrome/120 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9"
}

#Python creates storage.
all_products = []

#Program repeats 5 time - Page 1 Page 2 Page 3 Page 4 Page 5
for page in range(1,6):
    print("Scraping page",page)
    url = BASE_URL.format(page) #Build URL-url+page_no.
    response = requests.get(url,headers=HEADERS) #Python downloads HTML.
    soup = BeautifulSoup(response.text,"lxml")
    products=soup.select(".s-result-item")

    for item in products:
        name=item.select_one("h2")
        price=item.select_one(".a-price-whole")
        rating=item.select_one(".a-icon-alt")
 
        if name and price:
            all_products.append({
            "product_name":name.text.strip(),
            "price":price.text.strip(),
            "rating":rating.text.split()[0] if rating else None,
            "review_count":None,
            "platform":"Amazon",
            "date_scraped":datetime.now()
            })

    time.sleep(2)

df=pd.DataFrame(all_products)

print("Total scraped:",len(df))

print(df.head())

df.to_csv("../data/raw/products_raw.csv",index=False)

print("Scraping completed!")
# https://appbrewery.github.io/instant_pot/

from bs4 import BeautifulSoup
import pprint 
import requests
import os 
from dotenv import load_dotenv


url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

price_dollars = soup.find(name="span", class_="a-price-whole").getText().strip()
price_cents = soup.find(name="span", class_="a-price-fraction").getText().strip()

total_price = str(price_dollars) + str(price_cents)
print(total_price)


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

business_names = []
categories = []
links = []
locations = []

items = soup.find_all("article", class_="product_pod")

for item in items:

    name = item.h3.a["title"]

    link = item.h3.a["href"]

    category = "Retail"

    location = "Online"

    business_names.append(name)
    categories.append(category)
    links.append("https://books.toscrape.com/" + link)
    locations.append(location)

df = pd.DataFrame({
    "Business Name": business_names,
    "Category": categories,
    "Website": links,
    "Location": locations
})

df.to_excel("business_leads.xlsx", index=False)

print("Business leads exported successfully!")
import requests
from bs4 import BeautifulSoup

user_budget = int(input("What is your budget? Enter a whole number: "))

r = requests.get("https://www.johnlewis.com/john-lewis-partners-linear-medium-2-seater-sofa-bed-light-leg/p4263492")
content = r.content
print(content)
soup = BeautifulSoup(content)
element = soup.find("span", {"data-testid": "price-now", "class": "sofa-price__now"})

price = element.text.strip()
price_no_currency = price[1:]
price_number = float(price_no_currency)

if price_number > user_budget:
  print("This item is over your budget... Sorry!")
else:
  print("Lets buy it!")
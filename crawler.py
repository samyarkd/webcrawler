import requests
from bs4 import BeautifulSoup 
url = 'https://www.digikala.com/'

req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
soup = soup.find_all("a", class_ = 'js-carousel-ga-product-box')

for i in soup:
 print(i.get_text())

import requests
from bs4 import BeautifulSoup

#url = "https://www.domain.com.au/sale/sydney-region-nsw/?excludeunderoffer=1&ssubs=1&page=1"
url = "https://www.domain.com.au/4-ernesta-place-bella-vista-nsw-2153-2018695410"

headers={'User-Agent':
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)


html = BeautifulSoup(res.text, 'html.parser')

contact = html.find('a', {"data-testid" : "listing-details__phone-cta-button highlight"}, href=True)
print(contact['href'][4:])
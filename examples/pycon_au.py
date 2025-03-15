import requests
from bs4 import BeautifulSoup

response = requests.get('https://pycon.pyug.at/en/blog/')
soup = BeautifulSoup(response.text, 'html.parser')
for element in soup.find_all("h2"):
  print(element.text)


import requests
from bs4 import BeautifulSoup
import webbrowser
from rich import print

#random wikipedia article page
url = requests.get("https://en.wikipedia.org/wiki/special:Random")
#parse the content
soup = BeautifulSoup(url.content , 'html.parser')
#title of article
header = soup.find(id = 'firstHeading')
#short describe of article
describe = soup.find('p')

print("Here is the random article from wikipedia\n")
print(header.text,"\n")
print(describe.text)
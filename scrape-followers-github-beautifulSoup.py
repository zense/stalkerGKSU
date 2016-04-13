import requests
from bs4 import BeautifulSoup
import re
from threading import Thread

html = requests.get('https://github.com/'+username+'/followers')
htmltext = html.text
soup = BeautifulSoup(htmltext,'lxml')
results = soup.findAll('span',attrs={'class':'css-truncate css-truncate-target'})
print results


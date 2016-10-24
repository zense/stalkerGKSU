import requests
from bs4 import BeautifulSoup
import re
import sys

username = sys.argv[1]

def getfollowers(username):
        html = requests.get('https://github.com/'+username+'/followers').text
        regex = '<span class="css-truncate css-truncate-target" title="'+'(.+?)'+'"><a href="/'+'(.+?)'+'">'+'(.+?)'+'</a></span>'
        results = re.findall(re.compile(regex),html)

        """Finding using BeautifulSoup"""
        #soup = BeautifulSoup(htmltext,'lxml')
        #results = soup.findAll('span',attrs={'class':'css-truncate css-truncate-target'})
        print results


        """Get organisation from facebook"""

getfollowers()

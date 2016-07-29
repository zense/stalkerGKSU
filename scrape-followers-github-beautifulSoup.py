'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from github .
Description:
extracting followers using username of a user github account. For this I am using beautifulSoup and regex. 
'''

import requests
from bs4 import BeautifulSoup
import sys

def getFollowers():
	html = requests.get('https://github.com/'+sys.argv[1]+'/followers').text
	soup = BeautifulSoup(html,'lxml')
	for follower in soup.findAll('h3',attrs={'class':'follow-list-name'}):
		print follower.span.a['href'] , follower.span.a.getText()
		
getFollowers()

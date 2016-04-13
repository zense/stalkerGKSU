import requests
from bs4 import BeautifulSoup
import re
from threading import Thread
import sys
import logging
username = sys.argv[1]
html = requests.get('https://github.com/'+username+'/followers')
htmltext = html.text
regex = '<span class="css-truncate css-truncate-target" title="'+'(.+?)'+'"><a href="/'+'(.+?)'+'">'+'(.+?)'+'</a></span>'
pattern = re.compile(regex)
results = re.findall(pattern,htmltext)

"""Finding using BeautifulSoup"""
#soup = BeautifulSoup(htmltext,'lxml')
#results = soup.findAll('span',attrs={'class':'css-truncate css-truncate-target'})
print results


"""Get organisation from facebook"""
logging.basicConfig(level=logging.DEBUG)
s = requests.Session()
#html_fb = s.get('https://www.facebook.com')
data = {
        'email' : 'shreyakupadhyay07@gmail.com',
        'pass' : 'BlackHoleformat@123',
        }
headers = {
            ':authority':'www.facebook.com',
            ':method':'POST',
            ':path':'/login.php?login_attempt=1&lwv=110',
            ':scheme':'https',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding':'gzip, deflate',
            'accept-language':'en-US,en;q=0.8',
            'cache-control':'max-age=0',
            #'content-length':'796',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'datr=CbAIV4_NwCr-RDoGiCA25YlS; reg_fb_ref=https%3A%2F%2Fwww.facebook.com%2F; reg_fb_gate=https%3A%2F%2Fwww.facebook.com%2F; wd=1280x312; dpr=1.5',
            'origin':'https://www.facebook.com',
            'referer':'https://www.facebook.com',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36',

}
html_fb = s.post('https://www.facebook.com/login.php?login_attempt=1&lwv=110',data=data)
"""encoding data into ascii data from unicode data"""

htmltext_fb = html_fb.text
#print htmltext_fb
html_fb_head = html_fb.headers

#udata = data.decode("utf-8")
#asciidata = html_fb_head.encode("ascii","ignore")
print html_fb_head
#regex_fb = '<div class="_50f3">'+'(.+?)'+'<a class="profileLink" href="'+'(.+?)'+" data-hovercard="+'(.+?)'+'">'+'(.+?)'+'</a></div>'
#pattern_fb = re.compile(regex_fb)
#results_fb = re.findall(pattern_fb,htmltext_fb)
#soup_fb = BeautifulSoup(htmltext_fb,'lxml')
#results_fb = soup_fb.findAll('div',attrs={'class':'_50f3'})
#print results_fb

import requests
from bs4 import BeautifulSoup
import ast
import json
import warnings
warnings.filterwarnings("ignore")
class user:
    def __init__(self,name,followers_list,following_list):
        self.name=name
        self.followers_list=followers_list
        self.following_list=following_list
        

s=requests.Session()
#print s
r=s.get('https://github.com/'+'visheshruparelia'+'?tab=followers')
soup=BeautifulSoup(r.text)
data=soup.find_all("div",{"class":"d-table col-12 width-full py-4 border-bottom border-gray-light"})
primary=user("visheshruparelia",[],[])
secondary=[]
k=requests.Session()
for i in data:
    name=i.find_all("a")[0]['href']
    #print name
    #temp=k.get('https://api.github.com/users'+name)
    #print temp.text
    if 1:
        primary.followers_list.append(name)
print primary.followers_list
r=s.get('https://github.com/'+'visheshruparelia'+'?tab=following')
soup=BeautifulSoup(r.text)
data=soup.find_all("div",{"class":"d-table col-12 width-full py-4 border-bottom border-gray-light"})

#print temp.text
for i in data:
    name=i.find_all("a")[0]['href']
    #temp2=k.get('https://api.github.com/users'+'/'+i['login'])
    primary.following_list.append(name)
#print primary.following_list

for i in primary.followers_list:
    #print i
    r=s.get('https://github.com'+i+'?tab=followers')
    soup=BeautifulSoup(r.text)
    data=soup.find_all("div",{"class":"d-table col-12 width-full py-4 border-bottom border-gray-light"})
    temp_user=user(i,[],[])
    for i in data:
        name=i.find_all("a")[0]['href']
        print name
        temp_user.followers_list.append(name)
    secondary.append(temp_user)
#print primary.following_list
for i in primary.following_list:
    #print i
    r=s.get('https://github.com'+i+'?tab=following')
    soup=BeautifulSoup(r.text)
    data=soup.find_all("div",{"class":"d-table col-12 width-full py-4 border-bottom border-gray-light"})
    temp_user=user(i,[],[])
    for i in data:
        name=i.find_all("a")[0]['href']
        print name
        temp_user.following_list.append(name)
    secondary.append(temp_user)    
print primary.name,primary.following_list,primary.followers_list
for i in secondary:
    print i.name

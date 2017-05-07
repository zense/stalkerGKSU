import requests
from bs4 import BeautifulSoup
import warnings
import string
warnings.filterwarnings("ignore")

main_list = []
checked_list=[]

class user:
    def __init__(self,name,followers_list,following_list):
        self.name = name
        self.followers_list = followers_list
        self.following_list = following_list
        self.folllowing_node_list = []
        self.folllowers_node_list = []

def get_data(username, no):

    if no == 0:
        z = 'followers'
    else:
        z = 'following'

    s = requests.Session()
    r = s.get('https://github.com/' + username + '?tab='+z)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
    pages = soup.find_all("div", {"class" : "pagination"})
    final=[]

    x = 2
    while(pages != []):
        r = s.get('https://github.com/' + username + '?page=' +  str(x) + '&tab=' + z)
        soup = BeautifulSoup(r.text)
        data += soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
        pages = soup.find_all("div", {"class" : "pagination"})
        x += 1

    for i in data:
        name = i.find_all("a")[0]['href']
        try:
            company = i.find_all("span", {"class" : "mr-3"})[0].text.strip()
        except:
            company = "xxxxxxx"
        try:
            area = i.find_all("p", {"class" : "text-gray text-small mb-0"})[0].text.strip()
        except:
            area = "xxxxx"
        final.append([name,company,area])
    return final

def string_matching(name, mode, organisations, main_list):
    for org in organisations:
        try:
            if(mode in organisations):
                if name not in main_list:
                    main_list.append(name)
        except:
            pass

def scrape(username ,main_list):

    organisation = ["iiitb", "iiitbangalore", "internationalinstituteofinformationtechnologybangalore"]
    primary = user(username, [], [])
    secondary = []
    checked_list.append("/" + username)
    data = get_data(username,0)

    for i in data:
        name = i[0]
        company = (''.join(e for e in i[1] if e.isalpha())).lower()
        area = (''.join(e for e in i[2] if e.isalpha())).lower()
        string_matching(name,area,organisation,main_list)
        string_matching(name,company,organisation,main_list)

    data = get_data(username,1)

    for i in data:
        name = i[0]
        company = (''.join(e for e in i[1] if e.isalpha())).lower()
        area = (''.join(e for e in i[2] if e.isalpha())).lower()
        string_matching(name,area,organisation,main_list)
        string_matching(name,company,organisation,main_list)

    for j in primary.followers_list:

        checked_list.append(j)
        data = get_data(j,0)
        temp_user = user(j, [], [])

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)
        data = get_data(j,1)

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)
        primary.folllowers_node_list.append(temp_user)
        secondary.append(temp_user)

    for j in primary.following_list:

        if j not in checked_list:
            checked_list.append(j)

        data = get_data(j,1)
        temp_user = user(j, [], [])

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)

        primary.folllowing_node_list.append(temp_user)
        secondary.append(temp_user)
        data=get_data(j,0)

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)

def find(main_list,checked_list):
    for i in main_list:
        if i not in checked_list:
            scrape(i[1::],main_list)

def main():
        main_list=[]
        username = raw_input("Github username : ")
        scrape(username,main_list)
        find(main_list,checked_list)
        print main_list

if __name__ == '__main__':
        main()

import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")

main_list = []
checked_list = []

class user:
    def __init__(self, name, followers_list, following_list):
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

    # these lines of code gets the list of followers or the following on the first page
    # when there are no further pages of followers or following. And if there are go forward with the next page
    s = requests.Session()
    final = []
    x = 1
    pages = [""]
    data = []
    while(pages != []):
        r = s.get('https://github.com/' + username + '?page=' +  str(x) + '&tab=' + z) #first getting all the followers for z=0, and following for z=1
        soup = BeautifulSoup(r.text)
        data = data + soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
        pages = soup.find_all("div", {"class" : "pagination"})
        x += 1


   # getting company and area.
    for i in data:
        name = i.find_all("a")[0]['href']
        try:
            company = i.find_all("span", {"class" : "mr-3"})[0].text.strip()
        except:
            company = "xxxxx"
        try:
            area = i.find_all("p", {"class" : "text-gray text-small mb-0"})[0].text.strip()
        except:
            area = "xxxxx"
        final.append([name, company, area])
    return final

def string_matching(name, mode, organisations, main_list):
    for org in organisations:
        try:
            if(mode in organisations):
                if name not in main_list:
                    main_list.append(name)
        except:
            pass

def scrape_org(org,main_list,organisation):
    s = requests.Session()
    r = s.get('https://github.com/orgs/'+org+'/people')
    soup = BeautifulSoup(r.text)
    data = soup.find_all("div", {"class" : "table-list-cell py-3 pl-3 v-align-middle member-avatar-cell css-truncate pr-0"})
    for i in data:
        name = i.find_all("a")[0]['href']
        main_list.append(name)
    for i in main_list:
        r = s.get('https://github.com/'+i)
        soup = BeautifulSoup(r.text)
        data = soup.find_all("li",{"aria-label":"Organization"})
        try:
            org = (''.join(e for e in data[0].text if e.isalpha())).lower()
            if(org not in organisation):
                organisation.append(org)
        except:
            pass

# scraping the github pages
def scrape(username, main_list, organisation):
    primary = user(username, [], [])
    secondary = []
    checked_list.append("/" + username)
    data = get_data(username,0)   #calling get_data function with the given username as input and 0 = followers.
    data = data + get_data(username,1) #calling get_data function with the given username as input and 1 = followers.
    # data contains all the links to the profile url fo the followers and following

    for i in data:
        name = i[0]
        company = (''.join(e for e in i[1] if e.isalpha())).lower()  # removing all noise in the company name
        area = (''.join(e for e in i[2] if e.isalpha())).lower()   # removing all noise in the area name
        string_matching(name,area,organisation,main_list)  # checking area matches with the organisation or not
        string_matching(name,company,organisation,main_list) # checking area matches with the organisation or not


    # getting details about the first followers list.
    for j in primary.followers_list:
        checked_list.append(j)
        data = get_data(j,0) # getting data of the followers of the followers
        temp_user = user(j, [], [])

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)
        data = get_data(j,1) # getting data of the following of the followers

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
        data = get_data(j,1) # getting data of the following of the following
        temp_user = user(j, [], [])

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)
        primary.folllowing_node_list.append(temp_user)
        secondary.append(temp_user)
        data=get_data(j,0) # getting data of the followers of the following

        for i in data:
            name = i[0]
            company = (''.join(e for e in i[1] if e.isalpha())).lower()
            area = (''.join(e for e in i[2] if e.isalpha())).lower()
            string_matching(name,area,organisation,main_list)
            string_matching(name,company,organisation,main_list)

def find(main_list, checked_list, organisation):
    for i in main_list:
        if i not in checked_list:
            scrape(i[1::], main_list, organisation)  # recursion on every user who is not there in the main list.

def main(org):
        main_list=[]
        organisation=[]
        # org = raw_input("organisation name : ") #getting username as input
        scrape_org(org,main_list,organisation)
        find(main_list, checked_list, organisation)
        tmp = ""
        for usernames in main_list:
            tmp = tmp + usernames
        return tmp    
        # print len(main_list)

# program starts from here
if __name__ == '__main__':
        main()

import requests
from bs4 import BeautifulSoup
import warnings
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



def scrape(username = "gopuvenkat"):

	checked_list.append("/" + username)
	organisation = ["IIIT Bangalore", "IIITB", "iiitb", "@iiitb2014", "International Institute of Information Technology", "IIIT-Bangalore", "IIIT-B", "IIIT BANGALORE", "IIIT Bangalore, Electronic City Phase 1, Bengaluru, Karnataka", "International Institute of Information Technology Bangalore", "International Institute of Information Technology, Bangalore"]
	s = requests.Session()
	r = s.get('https://github.com/' + username + '?tab=followers')
	soup = BeautifulSoup(r.text)
	data = soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
	primary = user(username, [], [])
	secondary = []
	k = requests.Session()

	for i in data:
		name = i.find_all("a")[0]['href']
		company = i.find_all("span", {"class" : "mr-3"})
		area = i.find_all("p", {"class" : "text-gray text-small mb-0"})
		try:
			if(company[0].text.strip() in organisation):
				if (name  not  in primary.followers_list):
					primary.followers_list.append(name)
				if(name not in main_list):
					main_list.append(name)
		except:
			pass

		try:
			if(area[0].text.strip() in  organisation):
				if(name not in primary.followers_list):
					primary.followers_list.append(name)
				if(name not in main_list):
					main_list.append(name)
		except:
			pass

	# print primary.followers_list

	r = s.get('https://github.com/' + username + '?tab=following')
	soup = BeautifulSoup(r.text)
	data = soup.find_all("div", {"class":"d-table col-12 width-full py-4 border-bottom border-gray-light"})

	for i in data:
		name = i.find_all("a")[0]['href']
		company = i.find_all("span", {"class" : "mr-3"})
		area = i.find_all("p", {"class" : "text-gray text-small mb-0"})
		try:
			if(company[0].text.strip() in organisation):
				if(name not in primary.following_list):
					primary.following_list.append(name)
				if(name not in main_list):
					main_list.append(name)
		except:
			pass

		try:
			if(area[0].text.strip() in  organisation):
				if(name not in primary.following_list):
					primary.following_list.append(name)
				if(name not in main_list):
					main_list.append(name)
		except:
			pass

	# print primary.following_list
	for j in primary.followers_list:
		checked_list.append(j)
		r = s.get('https://github.com'+ j +'?tab=followers')
		soup = BeautifulSoup(r.text)
		data = soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
		temp_user = user(j, [], [])
		for i in data:
			name = i.find_all("a")[0]['href']
			company = i.find_all("span", {"class" : "mr-3"})
			area = i.find_all("p", {"class" : "text-gray text-small mb-0"})
			try:
				if(company[0].text.strip() in organisation):
					if name not in temp_user.followers_list:
						temp_user.followers_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
			try:
				if(area[0].text.strip() in  organisation):
					if(name not in temp_user.followers_list):
						temp_user.followers_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
		r = s.get('https://github.com' + j + '?tab=following')
		soup = BeautifulSoup(r.text)
		data = soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
		for i in data:
			name = i.find_all("a")[0]['href']
			company = i.find_all("span", {"class" : "mr-3"})
			area = i.find_all("p", {"class" : "text-gray text-small mb-0"})
			try:
				if(company[0].text.strip() in organisation):
					temp_user.following_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
			try:
				if(area[0].text.strip() in  organisation):
					if(name  not in temp_user.following_list):
						temp_user.following_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
		primary.folllowers_node_list.append(temp_user)
		secondary.append(temp_user)

	for j in primary.following_list:
		if j not in checked_list:
			checked_list.append(j)

		r = s.get('https://github.com' + j + '?tab=following')
		soup = BeautifulSoup(r.text)
		data = soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})
		temp_user = user(j, [], [])
		for i in data:
			name = i.find_all("a")[0]['href']
			company = i.find_all("span", {"class" : "mr-3"})
			area = i.find_all("p", {"class" : "text-gray text-small mb-0"})
			try:
				if(company[0].text.strip() in organisation):
					if name not in temp_user.following_list:
						temp_user.following_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
			try:
				if(area[0].text.strip() in organisation):
					if name not in temp_user.following_list:
						temp_user.following_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
		primary.folllowing_node_list.append(temp_user)
		secondary.append(temp_user)
		r = s.get('https://github.com'+ j +'?tab=followers')
		soup = BeautifulSoup(r.text)
		data = soup.find_all("div", {"class" : "d-table col-12 width-full py-4 border-bottom border-gray-light"})

		for i in data:
			name = i.find_all("a")[0]['href']
			company = i.find_all("span", {"class" : "mr-3"})
			area = i.find_all("p", {"class" : "text-gray text-small mb-0"})
			try:
				if(company[0].text.strip() in organisation):
					if(name not in temp_user.followers_list):
						temp_user.followers_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
			try:
				if(area[0].text.strip() in  organisation):
					if(name not in temp_user.followers_list):
						temp_user.followers_list.append(name)
					if(name not in main_list):
						main_list.append(name)
			except:
				pass
	# print main_list
	# print checked_list

def find(main_list,checked_list):
	for i in main_list:
		if i not in checked_list:
			scrape(i[1::])
			checked_list.append(i)

def main():
	username = raw_input("Github username : ")
	scrape(username)
	find(main_list,checked_list)
	print main_list

if __name__ == '__main__':
	main()

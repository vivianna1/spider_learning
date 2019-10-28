import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


def start_request(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,'lxml')
	# Tendering_unit = soup.find('tbody').find_all('tr')
	tr_list = soup.find('tbody').find_all('tr')
	data = {}
	for tr in tr_list:
		Tendering_unit = tr.find_all('span')[17].text.strip()
		print(Tendering_unit)



if __name__ == '__main__':
	url = 'http://www.hzctc.cn/AfficheShow/Home?AfficheID=40D3D23F-3ED4-452F-9FD9-FB04189A3704&IsInner=3&ModuleID=22'
	start_request(url)
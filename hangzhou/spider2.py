import requests
from bs4 import BeautifulSoup
import json

headers = {'Cookie':'UM_distinctid=16dfc53c589251-0a82e8a94c254c-b363e65-100200-16dfc53c58a23a; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1571994129; CNZZDATA5094733=cnzz_eid%3D1451057246-1571896412-%26ntime%3D1572001645; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1572001651',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

def start_request(url):
	data = {
		'area': '',
		'afficheType': 22,
		'IsToday':'', 
		'title': '',
		'proID': '',
		'number': '',
		'_search': 'false',
		'nd': 1572067168190,
		'rows': 10,
		'page': 1,
		'sidx': 'PublishStartTime',
		'sord': 'desc'
	}
	response = requests.post(url, data=data, headers=headers)
	soup = BeautifulSoup(response.content,'lxml')
	content = soup.find('body').find('p').text
	#print(soup)
	rows = json.loads(content)['rows']
	for row in rows:
		code_name = row['CodeName']
		tender_name = row['TenderName']
		tender_num = row['TenderNo']
		end_time = row['PublishEndTime']

		save_txt(code_name,tender_name,tender_num,end_time)
		print(code_name,tender_name,tender_num,end_time)

def save_txt(code_name,tender_name,tender_num,end_time):
	with open('hzzyjyw.txt','a+') as f:
		f.write(str(code_name) + ' ' + str(tender_name) + ' ' + str(tender_num) + ' ' + str(end_time) + '\n')
		f.close()


if __name__ == '__main__':
	url = 'https://www.hzctc.cn/SecondPage/GetNotice'
	start_request(url)
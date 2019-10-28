import requests
from bs4 import BeautifulSoup

def start_request(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,'lxml')
	district_id = soup.find('div',id='jqgh_gridData_CodeName')
	project_num = soup.find('div',id = 'jqgh_gridData_TenderNo')
	name_id = soup.find('div',id = 'jqgh_gridData_TenderName')
	time_id = soup.find('div',id = 'jqgh_gridData_PublishEndTime') 

	with open('file1','w') as f:
		f.write(str(district_id) + '\n')



if __name__ == '__main__':
	url = 'https://www.hzctc.cn/SecondPage/SecondPage?moduleID=67&ViewID=17&areaID=72'
	start_request(url)
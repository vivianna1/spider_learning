 import requests
import json
from bs4 import BeautifulSoup

headers = {'cookie':'__yadk_uid=QETtqFAOPjjJf8kLGSEhNCg2fPsDade8; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2; locale=zh-CN; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216de38e879c3d6-0ed408b28b67d4-b363e65-1049088-16de38e879d1fd%22%2C%22%24device_id%22%3A%2216de38e879c3d6-0ed408b28b67d4-b363e65-1049088-16de38e879d1fd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1571480932,1571481012,1571903790,1571971639; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1571971644; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1571971645; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1571971651',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


def start_request(url):
	response = requests.get(url,headers=headers)
	soup = BeautifulSoup(response.content,'lxml')
	li_list = soup.find('ul',class_='note-list').find_all('li')
	data = {}
	for li in li_list:
		title = li.find('a',class_='title').text.strip()
		title_id = li.find('a',class_='title')['href'].split('/')[-1]
		# title_url = 'https://www.jianshu.com/' + li.find('a',class_='title')['href']
		author = li.find('a',class_='nickname').text.strip()
		author_id = li.find('a',class_='nickname')['href']
		# author_url = 'https://www.jianshu.com/' + li.find('a',class_='nickname')['href']
		# print(author_id)
		comment_num = li.find('div',class_='meta').find_all('a')[1].text.strip()
		# comment_url = 'https://www.jianshu.com/' + comment_num
		# print(comment_num)
		# like_num = li.find('div',class_='meta').find_all('span')[1].text.strip()
		try:
			like_num = li.find('div',class_='meta').find_all('span')[1].text.strip()
		except Exception:
			like_num = 0
		# like_url = 'https://www.jianshu.com/' + like_num
		# print(like_num)
		# diamond_num = li.find('div',class_='meta').find_all('span')[0].text.strip()

		# diamond_url = 'https://www.jianshu.com/' + diamond_num
		try:
			diamond_num = li.find('div',class_='meta').find_all('span')[0].text.strip()
		except Exception:
			diamond_num = 0
		# print(diamond_num)

		data['author'] = author
		data['title'] = title
		data['comment_num'] = comment_num
		data['like_num'] = like_num
		data['diamond_num'] = diamond_num

def article_content(url,comment_num):
	res = requests.get(url,headers=headers)
	soup = BeautifulSoup(res.content,'lxml')
	read_num = soup.find('span',class_='_3tCVn5').find_all('span')[4].text.strip()
	read_url = 'https://www.jianshu.com/p/b785b56f1a07' + read_num
	print(read_num)


if __name__ == '__main__':
	url = 'https://www.jianshu.com/'
	start_request(url)


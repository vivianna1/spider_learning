import requests
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

def start_request(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    h2_list = soup.find('section',class_='nd-syllabus-term_cards ng-star-inserted')#.find_all('h2')
    print(h2_list)
    #date = {}
    #for h2 in h2_list:
        #title = h2.find('h2',class_ ='h3').text.strip()
        # title_id = h2.find('h2',class_='h3')
        # title_url = 'https://cn.udacity.com/course/business-analysis-nanodegree--nd100-cn?utm_source=youdao-jianshu&utm_medium=display&utm_campaign=band&utm_term=PC-youdao_dand&utm_content=jianshu-band-091103'
        # date['title'] = title
        # date['title_id'] = title_id
        # date['title_url'] = title_url
        # print(title)

if __name__ == '__main__':
    url = 'https://cn.udacity.com/course/business-analysis-nanodegree--nd100-cn?utm_source=youdao-jianshu&utm_medium=display&utm_campaign=band&utm_term=PC-youdao_dand&utm_content=jianshu-band-091103'
    start_request(url)

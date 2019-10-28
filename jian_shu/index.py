# -*- coding:utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': '_ga=GA1.2.1323902367.1500108642; read_mode=day; default_font=font2; locale=zh-CN; hibext_instdsigdip=1; _gid=GA1.2.1338869087.1536396682; hibext_instdsigdipv2=1; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1535091055,1535250251,1536396681,1536402519; remember_user_token=W1s1NTE4MzEyXSwiJDJhJDEwJE9LUU9jNC4xcEt2eXlzSExETjJoMWUiLCIxNTM2NDAyODgyLjIzNzI0NjUiXQ%3D%3D--f094ed2dd7e0f0c5e607c7d4e1cf10eb20106695; _m7e_session=0c1949c06fe7289423efa43aebe7fe90; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225518312%22%2C%22%24device_id%22%3A%2215f7d12b7f1255-0bcafb4b1e1c86-31657c03-1296000-15f7d12b7f2c5c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-collections%22%7D%2C%22first_id%22%3A%2215f7d12b7f1255-0bcafb4b1e1c86-31657c03-1296000-15f7d12b7f2c5c%22%7D; _gat=1; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1536406093',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

def start_request(url):
    """"""
    # 发起请求 简书需要添加headers
    response = requests.get(url, headers=headers)
    # 获取文章信息，用BeautifulSoup转成html
    soup = BeautifulSoup(response.content, "lxml")

    # 根据ul的class定位到所有的li 即文章的内容
    # find_all() 返回的是一个lsit对象
    li_list = soup.find('ul', class_='note-list').find_all('li')
    # li_list = soup.find('ul', id='xxx')
    data = {}
    # 循环获取每一篇文章内容信息
    for li in li_list:
        #print(li.text)
        title = li.find('a', class_='title').text.strip()
        # split()返回的是一个list对象
        # 根据属性获取对应的值 如li.find('a',class_='')['target']
        # find:根据属性定位,通常用class_=""或者id="" find_all
        # split() replace() strip() re：正则
        # 去空格：ss = ''.join(s.split(' '))
        title_id = li.find('a', class_='title')['href'].split('/')[-1]
        title_url = 'https://www.jianshu.com' + li.find('a', class_='title')['href']
        author = li.find('a', class_='nickname').text.strip()
        author_id = li.find('a', class_='nickname')['href'].split('/')[-1]
        author_url = 'https://www.jianshu.com' + li.find('a', class_='nickname')['href']
        comment_num = li.find('div', class_='meta').find_all('a')[1].text.strip()
        comment_url = 'https://www.jianshu.com' + li.find('div', class_='meta').find_all('a')[1]['href']
        like_num = li.find('div', class_='meta').find_all('span')[1].text.strip()
        data['title_id'] = title_id
        data['title'] = title
        data['author_id'] = author_id
        data['author'] = author
        data['comment_num'] = comment_num
        data['like_num'] = like_num
        # comment_list = article_content(title_url, int(comment_num))
        data['commtens'] = comment_list
        # print(comment_list)
        # print(data)
        # print(title_url, author_url, comment_url)
    

def article_content(url, comment_num):
    """爬取文章的详细内容"""
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    article = soup.find('article', class_='_2rhmJa').text.replace('图片发自简书App','').strip()
    article = ''.join(article.split())
    # print(article)
    # read_num = soup.find('span',class_='views-count')
    note_id = soup.find('meta', property="al:ios:url")['content'].split('/')[-1]
    all_page = int(comment_num / 10) + 1
    comment_list = []
    headers_1 = {
        'Cookie':'__yadk_uid=QETtqFAOPjjJf8kLGSEhNCg2fPsDade8; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1571903790,1571971639,1571975184,1572006565; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216de38e879c3d6-0ed408b28b67d4-b363e65-1049088-16de38e879d1fd%22%2C%22%24device_id%22%3A%2216de38e879c3d6-0ed408b28b67d4-b363e65-1049088-16de38e879d1fd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1571971644,1571975190,1572006572; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fu%2F62c7a150e860; _m7e_session_core=dda484950a3e7fafefad0b2482d74a3a; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1572006652; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1572006658',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    for i in range(all_page):
        data = {
            'page': i + 1,
            'count': 10,
            'author_only': 'false',
            'order_by': 'desc',  
        }
        content_url = 'https://www.jianshu.com/shakespeare/notes/' + str(note_id) + '/comments'
        print(content_url)
        con_res = requests.post(content_url, data=data,headers=headers_1)
        con_soup = BeautifulSoup(con_res.content, 'lxml')
        print(con_soup)
    #     comments = json.loads(con_soup.find('p').text)['comments']
    #     for comment in comments:
    #         # comment_id = comment['id']
    #         # compiled_content = comment['compiled_content']
    #         # user_id = comment['user_id']
    #         # nickname = comment['user']['nickname']
    #         # avatar = comment['user']['avatar']
    #         # is_author = comment['user']['is_author']
    #         comment_list.append(comment)
    #         # print(comment)
    # return comment_list

if __name__ == '__main__':
    #url = "https://www.jianshu.com"
    #start_request(url)
    comment_url = 'https://www.jianshu.com/p/d1b7dcfd7606'
    comment_num = 16
    article_content(comment_url, comment_num)

    # get 请求的时候 就是拼url
    'https://www.jianshu.com/shakespeare/notes/42569885/comments?page=1&count=10&author_only=false&order_by=desc'
    'https://www.jianshu.com/shakespeare/notes/d1b7dcfd7606/featured_comments?max_score=0&count=10'
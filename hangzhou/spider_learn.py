# 杭州公共资源交易网
import re
import requests
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Cookie": "UM_distinctid=16dfb6b9cef46c-0b7798106075c7-38677b00-1fa400-16dfb6b9cf0966; CNZZDATA5094733=cnzz_eid%3D1004106621-1571881196-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1571899554"
}
def start_request(url):
    # 数字不管 其他加成字符串
    # 72 本市 
    data = {
        'area': 72,
        'afficheType': 22,
        'IsToday': '',
        'title': '',
        'proID': '',
        'number': '',
        '_search': 'false',
        'nd': 1571904886668,
        'rows': 20,
        'page': 2,
        'sidx': 'PublishStartTime',
        'sord': 'desc',
    }
    response = requests.post(url, data=data, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    #print(soup)
    # <html><body><p>{xxxx}</p></body></html>
    content = soup.find('body').find('p').text
    # 把json格式转成字典
    rows = json.loads(content)['rows']

    #print(rows)

    for row in rows:
        code_name = row['CodeName']
        project_name = row['TenderName']
        project_num = row['TenderNo']
        project_date = row['PublishStartTime']
        project_id = row['ID']
        # 详情页url
        detail_url = 'http://www.hzctc.cn/AfficheShow/Home?AfficheID='+ str(project_id) + '&IsInner=0&ModuleID=22'
        print(detail_url)
        company_name, en_name, phone = pare_detail(detail_url)
        
        # 保存成text
        #save_txt(code_name, project_num, project_name, project_date)
        # print(code_name, project_num, project_name, project_date)

    
# def start_request_1(url):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, 'lxml')
#     print(soup)

def save_txt(code_name, project_num, project_name, project_date):
    with open('project.txt', 'a+') as f:
        f.write(str(code_name)+' ' + str(project_num) + ' ' + str(project_name) + ' '  + str(project_date) + '\n')
        f.close()

def pare_detail(url):
    """获取详情页信息"""
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find_all('table', class_='MsoNormalTable')
    company_name = ''
    en_name = ''
    phone = ''
    # 判断页面是否有数据
    if len(table) < 1:
        return company_name, en_name, phone
    tr_list = table[0].find_all('tr')
    company_name = tr_list[1].find_all('td')[1].text.strip()
    # 用正则判断 如果是数字 舍去
    com_names = re.findall('\d+', company_name)
    if len(com_names) == 1:
        print("错误的公司：" + str(company_name))
        company_name = ''
        return company_name, en_name, phone
    for tr in tr_list:
        title = tr.find_all('td')[0].text.strip()
        if '招标联系人' in title:
            en_name = tr.find_all('td')[1].text.strip()
            phone = tr.find_all('td')[3].text.strip()
    print(company_name, en_name, phone)
    return company_name, en_name, phone

if __name__ == '__main__':
    url = 'https://www.hzctc.cn/SecondPage/GetNotice'
    #url_1 = 'https://www.hzctc.cn/SecondPage/SecondPage?moduleID=67&ViewID=17&areaID=72'
    #start_request_1(url_1)
    start_request(url)
    detail_url = 'http://www.hzctc.cn/AfficheShow/Home?AfficheID=d0dc6d95-0bee-4018-95d3-c160a1eb7a2c&IsInner=0&ModuleID=22'
    #pare_detail(detail_url)
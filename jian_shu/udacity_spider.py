# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/10/22 21:52
@summary:
"""
import json
import requests
from bs4 import BeautifulSoup


def start_request(url):
    """"""
    # 发起请求 
    response = requests.get(url)
    # 获取文章信息，用BeautifulSoup转成html
    soup = BeautifulSoup(response.content, "lxml")
    section_list = soup.find_all("section", class_="nd-syllabus-term__cards ng-star-inserted")

    with open('jian_shu','w') as f:
        for section in section_list:
            title = section.find('h2').text.strip()
            f.write(title + '\n')

if __name__ == '__main__':
    url = "https://cn.udacity.com/course/business-analysis-nanodegree--nd100-cn?utm_source=youdao-jianshu&utm_medium=display&utm_campaign=band&utm_term=PC-youdao_dand&utm_content=jianshu-band-091103"

    start_request(url)
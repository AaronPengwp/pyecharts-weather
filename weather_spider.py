#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATS = []


def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')  # lxml的容错能力不够，在解释港澳台时不行
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        # for tr in trs:
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0].stripped_strings
            if index == 0:  # 首个不同
                city_td = tds[1].stripped_strings
            city = list(city_td)[0]
            temp_td = tds[-2].stripped_strings
            min_temp = list(temp_td)[0]
            # print({'city': city, 'min_temp': min_temp})
            ALL_DATS.append({'city': city, 'min_temp': int(min_temp)})  # 记得转化为数字，字符串排序有问题


def main():
    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"
    ]
    for url in urls:
        parse_page(url)

    # 分析数据
    # 根据最低气温进行排序
    ALL_DATS.sort(key=lambda data: data['min_temp'])
    # print(ALL_DATS)
    # 取前10个
    data = ALL_DATS[0:10]

    citys = list(map(lambda cy: cy['city'], data))
    temps = list(map(lambda t: t['min_temp'], data))

    # pyecharts
    # 安装pip install pyecharts
    # 详细使用网址：http://pyecharts.org/#/zh-cn/prepare
    chart = Bar("中国天气最低气温排行榜")
    chart.add('', citys, temps,is_more_utils=True)
    chart.render("temperatrue.html")


if __name__ == '__main__':
    main()

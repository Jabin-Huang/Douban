import requests
import re
import csv
from bs4 import BeautifulSoup

allInfo = []


def gethtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "fail to get html!"


def findinfo(soup):
    data = soup.find_all('div', {'class': 'info'})
    for info in data:
        unit_info = {}
        other = str(info.find('p', {'class': ""}))

        # 电影标题
        title = info.find('span', {'class': 'title'})
        if title.string == '大闹天宫':   # 该部电影的信息格式不合规范，难处理，故剔除
            continue
        else:
            unit_info['标题'] = title.string

            # group(1):上映时间，group(2):国家，group（3）：电影类型
            match = re.search('<br/>(.*?)/(.*?)/(.*?)</p>', str(other), re.S)
            unit_info['时间'] = " ".join(match.group(1).split())  # 将多余空白符删除。 split()无参数时，以空白符分割。
            unit_info['国家'] = " ".join(match.group(2).split())
            unit_info['类型'] = " ".join(match.group(3).split())

            # 电影摘引
            if info.find('span', {'class': 'inq'}):
                quote = info.find('span', {'class': 'inq'})
                unit_info['摘引'] = quote.string
            else:
                unit_info['摘引'] = ' '

            allInfo.append(unit_info)


def writecsv():
    with open('result.csv', 'wt', encoding='utf-16') as csvfile:
        csvout = csv.DictWriter(csvfile, ['标题', '时间', '国家', '类型', '摘引'])
        csvout.writeheader()
        csvout.writerows(allInfo)





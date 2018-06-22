from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from sources import info_count
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码


def country_pie():
    labels = []
    sizes = []
    othersize = 0
    explode = (0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    for (nation, times), i in zip(info_count.countrytimes_list, range(99999)):
        if i < 15:
            labels.append(nation)
            sizes.append(times)
        else:
            othersize += times
    labels.append('其它')
    sizes.append(othersize)
    colors = cm.rainbow(1 - np.arange(len(sizes)) / len(sizes))
    plt.figure(figsize=(12, 10))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title('豆瓣网TOP250电影制片国家/地区占比：')
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.savefig('country_pie.png')
    plt.show()


def type_pie():
    labels = []
    sizes = []
    othersize = 0
    explode = (0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    for (nation, times), i in zip(info_count.typetimes_list, range(99999)):
        if i < 15:
            labels.append(nation)
            sizes.append(times)
        else:
            othersize += times
    labels.append('其它')
    sizes.append(othersize)
    colors = cm.rainbow(1 - np.arange(len(sizes)) / len(sizes))
    plt.figure(figsize=(12, 10))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title('豆瓣网TOP250电影类型占比：')
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.savefig('type_pie.png')
    plt.show()


def year_pie():
    labels = []
    sizes =[]
    explode = (0.05, 0, 0, 0, 0, 0, 0, 0)
    for (year,times) in info_count.yeartimes_list:
        labels.append(year)
        sizes.append(times)
    colors = cm.rainbow(1 - np.arange(len(sizes)) / len(sizes))
    plt.figure(figsize=(12, 10))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title('豆瓣网TOP250电影上映年代占比：')
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.savefig('year_pie.png')
    plt.show()


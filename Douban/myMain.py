from sources import info_get,info_count,drawpie

url = 'https://movie.douban.com/top250'


def main():
    for i in range(10):
        html = info_get.gethtml(url + '?start=' + str(i * 25) + '&filter=')  # 网页共10页
        if html == "fail to get html!":
            print("fail to get html!")
            return -1
        soup = info_get.BeautifulSoup(html, "html.parser")
        info_get.findinfo(soup)
    info_get.writecsv()
    info_count.infocount()
    drawpie.country_pie()
    drawpie.type_pie()
    drawpie.year_pie()


main()
input()

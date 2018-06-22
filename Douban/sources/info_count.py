import csv


countrytimes = {}
typetimes = {}
yeartimes = {}
countrytimes_list = []
typetimes_list = []
yeartimes_list = []


# 统计国家，类型，所在年代次数
def infocount():
    with open('result.csv', 'rt', encoding='utf-16') as csvfile :
        reader = csv.DictReader(csvfile)

        for i in ['5', '6', '7', '8', '9']:
            yeartimes[i + '0年代'] = 0
        yeartimes['50年代前'] = 0
        yeartimes['21世纪00年代'] = 0
        yeartimes['21世纪10年代'] = 0

        for row in reader:
            for nation in row['国家'].split():
                if nation in countrytimes.keys():
                    countrytimes[nation] = countrytimes[nation] + 1
                else:
                    countrytimes[nation] = 1

            for type in row['类型'].split():
                if type in typetimes.keys():
                    typetimes[type] = typetimes[type] + 1
                else:
                    typetimes[type] = 1

            year = int(row['时间'])
            if 1949 < year < 1960:
                yeartimes['50年代'] = yeartimes['50年代'] + 1
            if 1959 < year < 1970:
                yeartimes['60年代'] = yeartimes['60年代'] + 1
            if 1969 < year < 1980:
                yeartimes['70年代'] = yeartimes['70年代'] + 1
            if 1979 < year < 1990:
                yeartimes['80年代'] = yeartimes['80年代'] + 1
            if 1989 < year < 2000:
                yeartimes['90年代'] = yeartimes['90年代'] + 1
            if 1999 < year < 2010:
                yeartimes['21世纪00年代'] = yeartimes['21世纪00年代'] + 1
            if 2009 < year < 2020:
                yeartimes['21世纪10年代'] = yeartimes['21世纪10年代'] + 1
            if year < 1950:
                yeartimes['50年代前'] = yeartimes['50年代前'] + 1

    # 排序
    countrytimes_list.extend(list(countrytimes.items()))
    typetimes_list.extend(list(typetimes.items()))
    yeartimes_list.extend(list(yeartimes.items()))
    countrytimes_list.sort(key=lambda x: x[1], reverse=True)
    typetimes_list.sort(key=lambda x: x[1], reverse=True)
    yeartimes_list.sort(key=lambda x:x[1], reverse=True)
    for tuples, i in zip(countrytimes_list, range(1, 99999)):
        print('country---- NO.'+str(i), tuples)
    for tuples, i in zip(typetimes_list, range(1, 99999)):
        print('type-------NO.'+str(i), tuples)
    for tuples, i in zip(yeartimes_list, range(1, 99999)):
        print('year---NO.'+str(i), tuples)








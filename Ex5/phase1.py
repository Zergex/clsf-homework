import lxml.html
import requests
import calendar
import datetime

site = 'http://lenta.ru'
rubrics = ['russia', 'world', 'ussr', 'economics', 'business',
           'forces', 'science', 'culture', 'sport', 'media', 'style', 'travel', 'life']

filenames = ['russia.txt', 'world.txt', 'ussr.txt', 'economics.txt', 'business.txt',
           'forces.txt', 'science.txt', 'culture.txt', 'sport.txt', 'media.txt', 'style.txt', 'travel.txt', 'life.txt']

years = [2015, 2016]

for yr in range(len(years)):
    for mn in range(1, 13):
        for ds in range(1, calendar.monthrange(years[yr], mn)[1] + 1):
            #    continue
            if datetime.date(years[yr], mn, ds) == (datetime.date.today() + datetime.timedelta(days=1)):
                break
            else:
                year = str(datetime.date(years[yr], mn, ds))[0:4]
                month = str(datetime.date(years[yr], mn, ds))[5:7]
                day = str(datetime.date(years[yr], mn, ds))[8:10]
            for rubs in range(len(rubrics)):
                response = requests.get(site + '/' + 'rubrics/' + rubrics[rubs] + '/' + year + '/' + month + '/' + day)
                tree = lxml.html.fromstring(response.text)
                links = tree.xpath('//div[@class="titles"]/h3/a/@href')
                for i in range(len(links)):
                    f = open(filenames[rubs], 'a', encoding="utf-8")
                    response = requests.get(site + links[i])
                    tree = lxml.html.fromstring(response.text)
                    news_title = tree.xpath('//div[@class="b-topic__content"]//h1/text()')
                    news_subtitle = tree.xpath('//div[@class="b-topic__content"]//h2[@class="b-topic__rightcol"]/text()')
                    news_text = tree.xpath('//div[@itemprop="articleBody"]/p/text()')
                    news_title = ' '.join(news_title)
                    news_subtitle = ' '.join(news_subtitle)
                    news_text = ' '.join(news_text)
                    f.write(news_title + '\n\n')
                    if news_subtitle == '':
                        pass
                    else:
                        f.write(news_subtitle + '\n\n')
                    f.write(news_text + '\n\n\n\n')
                    f.close()


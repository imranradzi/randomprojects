from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

country = input('country name goes here\n') + '/'
r = session.get('https://www.worldometers.info/coronavirus/country/' + country)
covidsoup = BeautifulSoup(r.text, 'html.parser')

maincontent = covidsoup.findAll('div', {'class': 'maincounter-number'})
index = 1
for i in maincontent:
    if index == 1:
        print('total covid cases')
    elif index == 2:
        print('current total deaths')
    elif index == 3:
        print('total recovered')
    print(i.span.text + '\n')
    index += 1
daily = covidsoup.find('div', {'class': 'news_date'})
print(daily.next_sibling.find('strong').text)

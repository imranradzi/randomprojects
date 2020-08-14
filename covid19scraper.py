from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

def countrycovidchecker(country):
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

running = True
while running:
    firstask = input('1. Direct search\n2. List search\nChoose search option (by typing the index)\n')
    if firstask == '1':
        country = input('Type the name of the country\n')
        try:
            countrycovidchecker(country)
        except:
            print('Invalid input, try again')
            continue

    elif firstask == '2':
        r1 = session.get('https://www.worldometers.info/coronavirus/#countries')
        countrysoup = BeautifulSoup(r1.text, 'html.parser')
        countries = countrysoup.findAll('a', {'class': 'mt_a'})
        countrylist = set()
        for i in countries:
            countrylist.add(i.text)

        initial = input('Type the initial letter of country\n').capitalize()
        index = 1
        tempcountrylist = []
        for i in countrylist:
            if str(i)[0] == initial:
                print(str(index) + ': ' +i)
                index += 1
                if str(i) == 'USA':
                    tempcountrylist.append('US')
                elif str(i) == 'UAE':
                    tempcountrylist.append('united-arab-emirates')
                else:
                    tempcountrylist.append(str(i))
        ask = input('Choose which (type index or country name)\n')
        asktype = 'unknown'
        try:
            int(ask)
        except:
            asktype = 'non-integer'
        else:
            asktype = 'integer'
        if asktype == 'non-integer':
            try:
                countrycovidchecker(ask)
            except:
                print('Invalid input, try again\n')
        elif asktype == 'integer':
            try:
                countrycovidchecker(tempcountrylist[int(ask)-1])
            except:
                print('Invalid input, try again\n')
                continue

    contloop = True
    while contloop:
        contornot = input('\nContinue? (Y/N)\n')
        if contornot == 'Y':
            contloop = False
            continue
        elif contornot == 'N':
            contloop = False
            running = False
        else:
            print('Invalid input, try again\n')

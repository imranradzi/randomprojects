from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

def countrycovidchecker(country):
    print(country + ' stats')
    r = session.get('https://www.worldometers.info/coronavirus/country/' + country) # url containing country's covid-19 stats
    covidsoup = BeautifulSoup(r.text, 'html.parser')

    maincontent = covidsoup.findAll('div', {'class': 'maincounter-number'}) # contains elements with the covid-19 stats we want
    index = 1
    for i in maincontent:
        if index == 1:
            print('Total covid cases')
        elif index == 2:
            print('Current total deaths')
        elif index == 3:
            print('Total recovered')
        print(i.span.text + '\n')
        index += 1
    daily = covidsoup.find('div', {'class': 'news_date'})
    print(daily.next_sibling.find('strong').text + ' (' + daily.text + ')') # current day's new cases

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
        countrylist = set() # technically a set
        # i use a set instead of a list here since there are duplicates of countries' names
        # in the html code
        for i in countries:
            countrylist.add(i.text) 

        initial = input('Type the initial letter of country\n').capitalize()
        # first letter of the countries' names are capitalized in the set so we need to
        # capitalize our input
        tempcountrylist = [] # list of countries starting with initial
        for i in countrylist:
            if str(i)[0] == initial:
                if str(i) == 'USA':
                    # few exceptions where the countries' names in the list don't match
                    # their url names
                    tempcountrylist.append('US')
                elif str(i) == 'UAE':
                    tempcountrylist.append('united-arab-emirates')
                else:
                    tempcountrylist.append(str(i))
        index = 1
        tempcountrylist.sort()
        for countryname in tempcountrylist:
            print(str(index) + '. ' + countryname)
            index += 1
        ask = input('Choose which (type index or country name)\n')
        asktype = 'unknown'
        try:
            # check to see if user input is an index or a country's name
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
    else:
        print('Invalid input, please try again')
        continue # loop resumes from the start if we don't pick any of the available options
        
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

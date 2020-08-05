from requests_html import HTMLSession

from bs4 import BeautifulSoup


session = HTMLSession()

running = True
while running:
    ask = input('which country\'s covid-19 stats for today would you like to know more about?\n')
    askcovid = ask + ' covid19 cases'
    par = {'q': askcovid}
    r = session.get('https://www.google.com/search', params=par)

    soooup = BeautifulSoup(r.text, 'html.parser')
    stats = soooup.findAll('td', {'jsname': 'VBiLTe'})

    index = 0
    for i in stats:
        caption1 = i.find('div').text
        stats1 = i.findAll('div')[1]
        try:
            stats1more = stats1.find('span').text
        except:
            stats1more = '---'
        else:
            stats1more = stats1.find('span').text
        print(caption1 + ': ' + stats1more)
        index += 1
        if index == 3:
            break

    print('\n')
    running1 = True
    while running1:
        end_or_not = input('terminate application? (yes or no)\n')
        if end_or_not == 'yes':
            running = False
            running1 = False
        elif end_or_not == 'no':
            print('ok')
            running1 = False
        else:
            print('invalid input, please try again')

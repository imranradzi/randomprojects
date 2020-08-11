from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()

running = True
while running:
    topic = input('what would you like to know about\n')
    r = session.get('https://en.wikipedia.org/wiki/' + topic)
    wikisoup = BeautifulSoup(r.text, 'html.parser')
    wikicontent = wikisoup.find('div', {'class': 'mw-parser-output'})
    try:
        wikicontent.findAll('p')
    except:
        print('no wikipedia page, perhaps there is a misspelling?\n')
    else:
        paragraphsprev = wikicontent.find('table')
        paragraphs = paragraphsprev.findNext('p').text
        print(paragraphs)
        askrunning = True
        while askrunning:
            ask = input('would you like to search for anything else? (yes or no)\n')
            if ask == 'no':
                askrunning = False
                running = False
                print('ending search')
            elif ask == 'yes':
                print('resuming search')
                askrunning = False
            else:
                print('invalid input, try again')


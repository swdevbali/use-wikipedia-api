import json
import requests
import bs4

print('Using Wikipedia API searching for any keyword')
keyword = 'batman'
url = f'https://en.wikipedia.org/w/api.php?action=parse&page={keyword}&format=json&prop=text&section=0'
try:
    response = requests.get(url)
    if response.status_code == 200:
        parse = json.loads(response.text)
        print('title = ', parse['parse']['title'])
        print('pageid = ', parse['parse']['pageid'])
        content = parse['parse']['text']['*']
        content = bs4.BeautifulSoup(content, features="html.parser")
        ps = content.findAll('p')
        for p in ps:
            print(f'{p.text}')

except Exception as ex:
    print(ex)

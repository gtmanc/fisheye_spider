import requests
from bs4 import BeautifulSoup

"""
Get a webpage in html by specified url.
Input: 
url: url to get
login: login information. [0]: name, [1]:password

Output: 
html in BeautifulSoup 
"""
def get_html(url, login):
    print('get url [{url_str}]'.format(url_str = url))
    #print(login[0] + login[1])

    r = requests.get(url, auth = (login[0], login[1]))

    if r.status_code == requests.codes.ok:
        #print("request ok!")
        soup = BeautifulSoup(r.text, 'html.parser')
    else:
        print("failed!")
        soup = None
    return soup  
import requests
from bs4 import BeautifulSoup

"""
Get a webpage in html by specified url.
Input: url
Output: html in BeautifulSoup 
"""
def get_html(url):
    print("Function: parse_html")

    r = requests.get(url, auth = ('JensonChin','13038Abc'))

    if r.status_code == requests.codes.ok:
        print("request ok!")
        soup = BeautifulSoup(r.text, 'html.parser')
    else:
        soup = None
    return soup
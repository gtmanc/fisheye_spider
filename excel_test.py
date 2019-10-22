from openpyxl import load_workbook
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup

import Constant
import get_html
import soup2list
import write2ws

"""
Before start to execute:
Use a command window to execute this script intead of the "run python in the terminal" at the right top corner in VS. 
No idea why it deosn't work.
"""

""" Preparations: create an worksheet with default names in 1st row """
""" Write first row wth default columns: Title, Date""" 
list[Constant.LIST_INDEX_TITLE] = 'Title'
list[Constant.LIST_INDEX_DATE] = 'Date'
list[Constant.LIST_INDEX_OBJECTIVES] = 'OBJECTIVES'
list[Constant.LIST_INDEX_PARTICIPATE1] = 'Participant1'
list[Constant.LIST_INDEX_PARTICIPATE2] = 'Participant2'
list[Constant.LIST_INDEX_PARTICIPATE3] = 'Participant3'
list[Constant.CELL_COMMENT] = 'Comment'
list[Constant.CELL_STATUS] = 'Status'
ws = write2ws.init(list)

""" create base url """
base_url = 'http://jira.altek.com.tw/fisheye/cru/'
project_id = 'NW3-'


""" Start to parse the reviews one by one"""
#r = requests.get(base_url + project_id + '1', auth = ('JensonChin','13038Abc'))
#rest = 'http://jira.altek.com.tw/fisheye/reviews-v1/'
#rest = 'http://jira.altek.com.tw/fisheye/cru/rest-service/reviews-v1/'
#r = requests.get(rest+'user-v1=?username=JensonChin')
#r = requests.get('http://jira.altek.com.tw/fisheye/cru/rest-service/reviews-v1?state=Review')
soup = get_html.get_html(base_url + project_id + '264')
list = soup2list.soup2list(soup)

#if r.status_code == requests.codes.ok:
#    print("request ok!")
#    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    
    #a_tags = soup.find_all('a')
    #for tag in a_tags:
    # 輸出超連結的文字
        # print(tag.string)
    #    print(tag.get('href'))
#print(soup.title.string)
#ws['A2'] = soup.title.string
    

wb.save('mainbuilding33.xlsx') #save it




# for i in range(1, 101):
#     for j in range(1, 101):
#         ws.cell(row = i, column = j, value = j)



# print(wb.sheetnames)


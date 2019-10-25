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
"""
Workseet name
TODO: These suppors to be entered by the user....
"""
wb_name = 'mainbuilding33.xlsx'
max_review = 2

""" Preparations: create an work book with default names in 1st row, default sheet """
""" Write first row with default columns""" 
list = ["", "", "", "", "", "", "", "", "", ""]
list[Constant.LIST_INDEX_TITLE] = 'Title'
list[Constant.LIST_INDEX_DATE] = 'Date'
list[Constant.LIST_INDEX_OBJECTIVES] = 'OBJECTIVES'
list[Constant.LIST_INDEX_PARTICIPATE1] = 'Participant1'
list[Constant.LIST_INDEX_PARTICIPATE2] = 'Participant2'
list[Constant.LIST_INDEX_PARTICIPATE3] = 'Participant3'
list[Constant.LIST_INDEX_COMMENT] = 'Comment'
list[Constant.LIST_INDEX_STATUS] = 'Status'
wb = write2ws.init(list)
ws = wb.active #get a defult sheet, will be used later
""" create base url """
base_url = 'http://jira.altek.com.tw/fisheye/cru/'
project_id = 'NW3-'


""" Start to parse the reviews and write the interesting tag string to worksheet one by one"""
#r = requests.get(base_url + project_id + '1', auth = ('JensonChin','13038Abc'))
#rest = 'http://jira.altek.com.tw/fisheye/reviews-v1/'
#rest = 'http://jira.altek.com.tw/fisheye/cru/rest-service/reviews-v1/'
#r = requests.get(rest+'user-v1=?username=JensonChin')
#r = requests.get('http://jira.altek.com.tw/fisheye/cru/rest-service/reviews-v1?state=Review')
#basic test:NW-1, NW-264
for i in range(max_review):
    index = i + 1
    print('parse review[{num}]...'.format(num = project_id + str(index)), end=':')
    soup = get_html.get_html(base_url + project_id + str(index))
    if soup != None:
        print('OK')
        list = soup2list.soup2list(soup)
        write2ws.write2ws(list, ws, index+1)    #first row needs to be kept. so, index must be increased by 1
    else:
        print('Failed!')
        
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
    

wb.save(wb_name) #save it




# for i in range(1, 101):
#     for j in range(1, 101):
#         ws.cell(row = i, column = j, value = j)



# print(wb.sheetnames)


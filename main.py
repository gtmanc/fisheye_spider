from openpyxl import load_workbook
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup

import Constant
import get_html
import html_parser
import write_ws
import pw_manager

"""
Before start to execute:
Use a command window to execute this script intead of the "run python in the terminal" at the right top corner in VS. 
No idea why it deosn't work.
"""
"""
Start to ask the necessary inputs
1. Account and password
2. Worksheet name
3. Maximum number of ticket to be downloaded
"""
login_info = ['','']
login_info[0] = input("Please enter account:")
print("Please enter password:")
login_info[1] = pw_manager.pwd_input()
#print(login_info[0] + login_info[1])

wb_name = input('Enter worksheet name. Or press Enter to use defult name (Review_report.xlsx))')
if wb_name in '\r\n': 
    wb_name = 'Review_report.xlsx'

max_review = input('Enter maximum number of ticket to be downloaded. Or press Enter to use defult number (400))')
if max_review in '\r\n':
    max_review = 400
else:
    max_review = int(max_review)
#max_review = 1
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
wb = write_ws.init(list)
ws = wb.active #get a defult sheet, will be used later
""" create base url """
base_url = 'http://jira.altek.com.tw/fisheye/cru/'
project_id = 'NW3-'


""" Start to parse the reviews and write the interesting tag string to worksheet one by one"""
for i in range(max_review):
    index = i + 1
    #index = 375
    print('parse review [{num}] '.format(num = project_id + str(index)), end=': ')
    soup = get_html.get_html(base_url + project_id + str(index), login_info)
    if soup != None:
        print('OK')
        list = html_parser.soup2list(soup)
        write_ws.write2ws(list, ws, index+1)    #first row needs to be kept. so, index must be increased by 1
    else:
        print('Get url failed! skip this url...')
        continue

wb.save(wb_name) #save it

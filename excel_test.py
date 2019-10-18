from openpyxl import load_workbook
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup

import Constant
import get_html
import soup2list

"""
Before start to execute:
Use a command window to execute this script intead of the "run python in the terminal" at the right top corner in VS. 
No idea why it deosn't work.
"""

""" Preparations: create an worksheet and url """
wb = Workbook()
#wb = load_workbook('mainbuilding33.xlsx')
ws = wb.active #get a defult sheet
#print(ws.title)
# ws.title = "first" #give a name to a sheet
# ws2 = wb.create_sheet("my_sheet") #create a new sheet
# ws = wb["first"] #get a heet with a specified name
""" Write first row wth default columns: Title, Date""" 
ws[Constant.CELL_TITLE] = 'Title'
ws[Constant.CELL_DATE] = 'Date'
ws[Constant.CELL_PARTICIPATE] = 'Participant'
ws[Constant.CELL_COMMENT] = 'Comment'

""" create base url """
base_url = 'http://jira.altek.com.tw/fisheye/cru/'
project_id = 'NW3-'


""" Start to parse the reviews one by one"""
#r = requests.get(base_url + project_id + '1', auth = ('JensonChin','13038Abc'))
#rest = 'http://jira.altek.com.tw/fisheye/reviews-v1/'
#rest = 'http://jira.altek.com.tw/fisheye/cru/rest-service/reviews-v1/'
#r = requests.get(rest+'user-v1=?username=JensonChin')
#r = requests.get('http://jira.altek.com.tw/fisheye/cru/rest-service/reviews-v1?state=Review')
soup = get_html.get_html(base_url + project_id + '1')
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


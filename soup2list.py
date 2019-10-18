import Constant

list = ["", "", "", "", ""]

"""parse soup and copy the interested ting to the list"""
def soup2list(soup):
    #Title
    list[Constant.LIST_INDEX_TITLE] = soup.title.string
    #list[0] = soup.title.string

    #DATE
    tag = soup.find('time')
    list[Constant.LIST_INDEX_DATE] = tag.get('title')
    #print(tag.get('title'))

    #Objectives
    tag = soup.find(class_ = 'meta-objectives')
    list[Constant.LIST_INDEX_DATE] = tag.text
    #print(tag.text)

    #Participant
    tags = soup.find_all("a", class_ = 'user avatar userorcommitter-parent')
    list_start = Constant.LIST_INDEX_PARTICIPATE1
    for tag in range(len(tags)):
        #print(tags[tag].string)
        #print(list_start + tag)
        list[list_start + tag] = tags[tag].string

    #General comment
    tag = soup.find(id = 'general-comments')


    return list

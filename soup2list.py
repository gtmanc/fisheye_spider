import Constant

list = ["", "", "", "", "", "", "", "", "", ""]

"""parse soup and copy the interested ting to the list"""
def soup2list(soup):
    #print(soup.prettify())

    #Title
    if soup.title == None:
        print('No title found')
    list[Constant.LIST_INDEX_TITLE] = soup.title.string
    #list[0] = soup.title.string
    #print(soup.title.string)

    #Revew status
    tag = soup.find(class_ = 'class="aui-lozenge aui-lozenge-success')
    #tag = soup.find(id = 'review-state')
    if tag == None:
        print('No status found')
    #print(tag.text)
    list[Constant.LIST_INDEX_STATUS] = tag.text

    #DATE
    #if a review is closed, search tag "span" instead of 'time'
    if tag.text == open:
        tag = soup.find('time')
    else:
        tag = soup.find('span')

    if tag == None:
        print('No date found')
    list[Constant.LIST_INDEX_DATE] = tag.get('title')
    #print(tag.get('title'))

    #Objectives
    #TODO: need to figure out how to handle the case that there is no objective
    #tag = soup.find(class_ = 'meta-objectives')
    tag = soup.find(id = 'objectives-markup')
    list[Constant.LIST_INDEX_DATE] = tag.text
    print(tag.text)

    #Participant
    tags = soup.find_all("a", class_ = 'user avatar userorcommitter-parent')
    list_start = Constant.LIST_INDEX_PARTICIPATE1
    for tag in range(len(tags)):
        print(tags[tag].string)
        #print(list_start + tag)
        list[list_start + tag] = tags[tag].string

    #General comment
    #TODO: Currently only the fitst comment is written. Need to think about how to write all of the comments to a cell
    tag = soup.find(class_ = 'comment-content markup')
    if tag == None:
        tag = soup.find(id = 'no-general-comments')
    print(tag.text)
    list[Constant.LIST_INDEX_COMMENT] = tag.text
    
    

    
    for item in list:
        print(item)
    

    return list

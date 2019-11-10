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
    tag = soup.find(id = "review-state")#, (class_ = 'class="aui-lozenge aui-lozenge-success')
    if tag == None:
        print('No status found')
    #print(tag.text)
    list[Constant.LIST_INDEX_STATUS] = tag.text

    #DATE
    #if a review is closed, search tag "span" instead of 'time'
    if tag.text == 'open' or tag.text == 'draft':
        name = 'time'
    else:
        name = 'span'    
    tag = tag.find_next_siblings(name)
    if tag == None:
        print('No date found')

    #print('len={len}'.format(len = len(tag)))
    #print(tag[0].get('title'))
    
    #There could be many matched searches. But only the fist is interested.
    list[Constant.LIST_INDEX_DATE] = tag[0].get('title')
    

    #Objectives
    #TODO: need to figure out how to handle the case that there is no objective
    #tag = soup.find(class_ = 'meta-objectives')
    tag = soup.find(id = 'objectives-markup')
    if tag == None:
        print('No objective found')
    list[Constant.LIST_INDEX_OBJECTIVES] = tag.text

    #Participant
    tags = soup.find_all("a", class_ = 'user avatar userorcommitter-parent')
    if tags == None:
        print('No Participant found')
    list_start = Constant.LIST_INDEX_PARTICIPATE1
    i = 0
    for tag in range(len(tags)):
        #print(tags[tag].string)
        #print(list_start + tag)
        list[list_start + tag] = tags[tag].string
        i = i + 1
        if i > Constant.MAX_PARTICIPATE: #if more than max participate we have, skip it
            continue


    #General comment
    #TODO: Currently only the lastest comment is written. Need to think about how to write all of the comments to a cell
    tag = soup.find_all(class_ = 'comment-content markup')
    if len(tag) != 0:
        comment = tag[len(tag)-1]
        comment_text = comment.text
    else:
        print('No comment found')
        comment_text = 'There is no general comment' #soup.find(id = 'no-general-comments') 
    
    #print(tag.text)
    list[Constant.LIST_INDEX_COMMENT] = comment_text
    
    #for item in list:
    #    print(item)
    
    return list

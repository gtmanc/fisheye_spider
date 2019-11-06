#Cell number for 1st row
CELL_TITLE = 'A1'
CELL_DATE = 'B1'
CELL_OBJECTIVES = 'C1'
CELL_PARTICIPATE1 = 'D1'
CELL_PARTICIPATE2 = 'E1'
CELL_PARTICIPATE3 = 'F1'
CELL_COMMENT = 'G1'
CELL_STATUS = 'H1'


# Index of the list which is used as the input of excel writer
LIST_INDEX_TITLE = 0
LIST_INDEX_DATE = LIST_INDEX_TITLE + 1
LIST_INDEX_OBJECTIVES = LIST_INDEX_DATE + 1
LIST_INDEX_PARTICIPATE1 = LIST_INDEX_OBJECTIVES + 1
LIST_INDEX_PARTICIPATE2 = LIST_INDEX_PARTICIPATE1 + 1
LIST_INDEX_PARTICIPATE3 = LIST_INDEX_PARTICIPATE2 + 1
LIST_INDEX_COMMENT = LIST_INDEX_PARTICIPATE3 + 1
LIST_INDEX_STATUS = LIST_INDEX_COMMENT + 1

MAX_PARTICIPATE = LIST_INDEX_PARTICIPATE3 - LIST_INDEX_PARTICIPATE1 + 1
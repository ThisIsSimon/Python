'''
Code that utilizes BeautifulSoup to parse excel xml
'''

file = open(filename).read()
soup = BeautifulSoup(file,'xml')
workbook = []
for sheet in soup.findAll('Worksheet'): 
    sheet_as_list = []
    for row in sheet.findAll('Row'):
        row_as_list = []
        for cell in row.findAll('Cell'):
            row_as_list.append(cell.Data.text)
        sheet_as_list.append(row_as_list)
    workbook.append(sheet_as_list)

'''
Simple application that dumps a specific excel formatted file into a SQL Server database. This small application starts by asking the
user to select a file. It then reads from very specific tabs and appropriately loops the data into a list. Finally, it makes a 
database connection and proceeds to dump everything into the database. 

Important notes:
If your database has an INT value, uploading empty values will cause errors. You can bypass this by reiterating over the list
and add in NULL for those appropriate areas.

Sometimes a certain tab will be completely empty and this will cause an error. There is a history of empty tabs causing errors,
I by passed this by adding in a try, except and pass on some.

This is one of my first applications I've written out of college and it's ugly as hell, but it works.
'''
from Tkinter import *
from tkFileDialog import askopenfilename
import os
import datetime

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#print(filename)
excel_filename = os.path.basename(filename) #get the actual file name from the directory path for uploading purposes

from openpyxl import load_workbook
workbook = load_workbook(filename, data_only=True)

print "Reading file..."

#########Sheet titled Changes#########
Changes_values = []

sheet_changes = workbook.get_sheet_by_name('Changes')

row_count_c = sheet_changes.max_row #determines the *.max_row count
column_count_c = sheet_changes.max_column #determines the *.column_row count

for row in sheet_changes.iter_rows(min_row = 2, max_col = column_count_c, max_row = row_count_c):
    Changes_values.append(str(datetime.date.today()) + '_' + excel_filename) #For datetime: datetime.datetime.now()
    Changes_values.append(excel_filename)
    Changes_values.extend(filter(None, [cell.value for cell in row]))      
    ##print[cell.value for cell in row]

it_changes = iter(Changes_values)
it_changes = [iter(Changes_values)] * 12
Changes_values = zip(*it_changes)

#print Changes_values

#########END#########

#########Sheet titled Fatal Exceptions#########
    
Fatal_Exception_values = []

sheet_Fatal_Exceptions = workbook.get_sheet_by_name('Fatal Exceptions')

#here you iterate over the rows in the specific column
for row in range(2,sheet_Fatal_Exceptions.max_row):
    Fatal_Exception_values.append(str(datetime.date.today()) + '_' + excel_filename)
    Fatal_Exception_values.append(excel_filename)
    for column in "ABCDEFGIJ":  #Here you can add or reduce the columns
        cell_name = "{}{}".format(column, row)
        Fatal_Exception_values.append(sheet_Fatal_Exceptions[cell_name].value) # the value of the specific cell        

       
it_fev = iter(Fatal_Exception_values)
it_fev = [iter(Fatal_Exception_values)] * 11
Fatal_Exception_values = zip(*it_fev)

#########END#########

#########Sheet titled Tolerable Exceptions#########
    
Tolerable_Exceptions_values = []

sheet_Tolerable_Exceptions = workbook.get_sheet_by_name('Tolerable Exceptions')

row_count_te = sheet_Tolerable_Exceptions.max_row #determines the *.max_row count
column_count_te = sheet_Tolerable_Exceptions.max_column #determines the *.column_row count


for row in sheet_Tolerable_Exceptions.iter_rows(min_row = 2, max_col = column_count_te, max_row = row_count_te):
    Tolerable_Exceptions_values.append(str(datetime.date.today()) + '_' + excel_filename)
    Tolerable_Exceptions_values.append(excel_filename)
    Tolerable_Exceptions_values.extend(filter(None, [cell.value for cell in row]))
    ##print[cell.value for cell in row]

it_tev = iter(Tolerable_Exceptions_values)
it_tev = [iter(Tolerable_Exceptions_values)] * 11
Tolerable_Exceptions_values = zip(*it_tev)

#print Tolerable_Exceptions_values

#########END#########


#########Sheet titled Dropped Records#########
    
DroppedRecords_values = []

sheet_DroppedRecords = workbook.get_sheet_by_name('Dropped Records') #Name of tab

row_count_dr = sheet_DroppedRecords.max_row #determines the *.max_row count
column_count_dr = sheet_DroppedRecords.max_column #determines the *.column_row count


for row in sheet_DroppedRecords.iter_rows(min_row = 2, max_col = column_count_dr, max_row = row_count_dr):
    DroppedRecords_values.append(str(datetime.date.today()) + '_' + excel_filename)
    DroppedRecords_values.append(excel_filename)
    DroppedRecords_values.extend(filter(None, [cell.value for cell in row]))
    ##print[cell.value for cell in row]

it_dr = iter(DroppedRecords_values)
it_dr= [iter(DroppedRecords_values)] * 9
DroppedRecords_values = zip(*it_dr)

#print DroppedRecords_values

#########END#########

print "File read, making database connection..."


import pyodbc
    
insert_conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 11 for SQL Server};'
    r'SERVER=SERVER;'
    r'DATABASE=DATABASE;'
    r'Trusted_Connection=yes;' #this is used for windows authentication
    )
print "Database connection successful, uploading items now..."
insert_table = insert_conn.cursor()
try:
    insert_table.executemany("insert into ASO_Electronic_Upload_StagingTable (BatchloadID, Excel_Filename, Employee_ID, SSN, Last_Name, First_Name, Relationship, Date_of_Birth, Carrier_ID_Numbers, Exceptions, Occurences, Source, Upload_Date, Current_Status, ItemSource) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'ASO Electronic Files', getdate(), '1', '36');", Fatal_Exception_values)
except Exception as e:
    print e
print "25%..."
try:
    insert_table.executemany("insert into ASO_Electronic_Upload_StagingTable (BatchloadID, Excel_Filename, Employee_ID, SSN, Last_Name, First_Name, Relationship, Date_of_Birth, Carrier_ID_Numbers, Exceptions, Number_of_Times_Issue_Has_been_Recorded, Source, Upload_Date, Current_Status, ItemSource) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'ASO Electronic Files', getdate(), '1', '36');", Tolerable_Exceptions_values)
except Exception as e:
    print e
print "50%..."
try:
    insert_table.executemany("insert into ASO_Electronic_Upload_StagingTable (BatchloadID, Excel_Filename, Employee_ID, SSN, Last_Name, First_Name, Relationship, Date_of_Birth, Carrier_ID_Numbers, Change, Effective_Date, Fields_Updated, Source, Upload_Date, Current_Status, ItemSource) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, 'ASO Electronic Files', getdate(), '1', '36');", Changes_values)
except Exception as e:
    print e
try:
    insert_table.executemany("insert into ASO_Electronic_Upload_StagingTable (BatchloadID, Excel_Filename, Employee_ID, SSN, Last_Name, First_Name, Relationship, Date_of_Birth, Carrier_ID_Numbers, Source, Upload_Date, Current_Status, ItemSource) values (?, ?, ?, ?, ?, ?, ?, ?, ?, 'ASO Electronic Files', getdate(), '1', '36');", DroppedRecords_values)
except Exception as e:
    print e
    pass
try:
    insert_table.execute("execute ASO_Electronic_Files_StagingAndDueDate_StoredProcedure")
except Exception as e:
    print e
    
print "75%..."
insert_table.commit()
print "100%..."

insert_table.close()
print "File Uploaded"
print "Press Enter to exit"


raw_input()


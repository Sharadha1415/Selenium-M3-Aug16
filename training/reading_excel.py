'''
xlrd    :   To read the excel files, we use xlrd

To install xlrd
    Go to command prompt    --> pip install xlrd==1.2.0

'''

import xlrd

## open the excel file
path = r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\M3_data.xlsx'
workbook = xlrd.open_workbook(path)
# print(workbook)             ## book object

## open the worksheet
worksheet = workbook.sheet_by_name('candidates_info')
# print(worksheet)            ##  Sheet object

## convert the sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)                 ## generator object

##----------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele)
#
# ## [text:'name', text:'place', text:'email_id', text:'phone_num']
# ## [text:'Shailaja', text:'Bengaluru', text:'shailaja@gmail.com', text:'9080706050']
# ## [text:'Deeksha', text:'Chennai', text:'deeksha@gmail.com', text:'9181716151']
# ## [text:'Hashmath', text:'Hyderabad', text:'hashmath@gmail.com', text:'9282726252']
# ## [text:'Atharva', text:'Pune', text:'atharva@gmail.com', text:'9876987655']

##----------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0], ele[1], ele[2], ele[3])
#
# ## text:'name' text:'place' text:'email_id' text:'phone_num'
# ## text:'Shailaja' text:'Bengaluru' text:'shailaja@gmail.com' text:'9080706050'
# ## text:'Deeksha' text:'Chennai' text:'deeksha@gmail.com' text:'9181716151'
# ## text:'Hashmath' text:'Hyderabad' text:'hashmath@gmail.com' text:'9282726252'
# ## text:'Atharva' text:'Pune' text:'atharva@gmail.com' text:'9876987655'

##----------------------------------------------------------------------------------------
for ele in rows:
    print(ele[0].value, ele[1].value, ele[2].value, ele[3].value)

## name place email_id phone_num
## Shailaja Bengaluru shailaja@gmail.com 9080706050
## Deeksha Chennai deeksha@gmail.com 9181716151
## Hashmath Hyderabad hashmath@gmail.com 9282726252
## Atharva Pune atharva@gmail.com 9876987655


















































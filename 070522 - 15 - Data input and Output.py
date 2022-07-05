'''
    Data input and output:
        CSV
        Excel
        HTML
        SQL

    Install the libraries
        pip install sqlalchemy
        pip install lxml
        pip install html5lib
        pip install BeautifulSoup4
        pip install xlrd
'''

from operator import index
import pandas as pd

# Reading Excel File

df = pd.read_excel(r'C:\Python\Udemy Data Science - Python\Excel_Sample.xlsx',sheet_name='Sheet1')
print(df)
df.to_excel('Output_excel.xlsx', sheet_name='New_sheet')
# pd.read_excel('Output_excel.xlsx')



# Reading HTML File

# df_html = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
# print(df_html[0])
# print(df_html[0].head())


# Writing to SQL
from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:")

df.to_sql('my_table',engine)

sqldf = pd.read_sql('my_table', con= engine)

print(sqldf)
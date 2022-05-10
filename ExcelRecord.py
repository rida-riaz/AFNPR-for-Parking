import os
from tkinter import*
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
#from matplotlib import image
from tkinter import ttk
import pymysql
#import xlrd
#import pandas.io.sql as sql
from pymysql import*
#import xlwt
#import pandas.io.sql as sql
import pandas as pd
import xlsxwriter
import pyodbc
import xlwt
import pandas.io.sql as sql
# connect the mysql with the python
con=connect(user="root",password="",host="localhost",database="nfr")
# read the data
df=sql.read_sql('select * from driver_registration_form',con)
# print the data
print(df)
# export the data into the excel sheet
#df.to_excel(sheet_name = "drivers-record.xlsx", header = True, index = False)
with pd.ExcelWriter("drivers-record.xlsx", engine="xlsxwriter", options = {'strings_to_numbers': True, 'strings_to_formulas': False}) as writer:
        try:
            df = pd.read_sql("Select * from driver_registration_form", con)
            df.to_excel(writer, sheet_name = "drivers-record.xlsx", header = True, index = False)
            print("File saved successfully!")
        except:
            print("There is an error")
root=Tk()
root.mainloop()
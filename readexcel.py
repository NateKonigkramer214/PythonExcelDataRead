
import pandas as pd

def  read_excel(filepath, column):
    dataframe = pd.read_excel(filepath, usecols = column)
    return dataframe
#Vars
column = [0, 1]
filepath = 'D:\Python_Excel\TestData2.xlsx' 
dataframe = read_excel(filepath, column)
print(dataframe)

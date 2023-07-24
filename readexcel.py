
import pandas as pd

def  read_excel(filepath, column):
    dataframe = pd.read_excel(filepath, usecols = column)
    return dataframe
#Vars
column = [1, 1]
filepath = 'D:\Python_Excel\TestData.xlsx' 
dataframe = read_excel(filepath, column)
print(dataframe)


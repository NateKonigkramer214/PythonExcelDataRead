
import pandas as pd

def  read_excel(filepath, column):
    dataframe = pd.read_excel(filepath, usecols = column)
    return dataframe
#Vars
column = [0, 1]
filepath = 'D:\Python_Excel\TestData3.xlsx' 
dataframe = read_excel(filepath, column)
print(dataframe)
print("")
sorted_date = dataframe.sort_values(by='Price')
print("Sorted Data: ")
print(sorted_date)
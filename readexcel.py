"""

Nathan Konigkramer

"""
# Import the pandas

import pandas as pd

# Column varible 
col = [1, 1]

# Read the 'TestData.xlsx' file located at 'D:\Python_Excel\TestData.xlsx'
# and store the data in a pandas DataFrame 
dataframe = pd.read_excel('D:\Python_Excel\TestData.xlsx', usecols= col) # added the usecols to read from a column defined by var "col"

# Print the contents of the DataFrame 'df'
print(dataframe)



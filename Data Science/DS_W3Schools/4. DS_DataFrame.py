#Creating Data Frame with Pandas

import pandas as pd
#panda was not friendly to me
#Reminder:
#pip install pandas in Command Prompt, select interpreter for python in VS Code

#d: dictionary, df: data frame
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data = d)

print(df)

#Expected Output
#    col1  col2  col3
#0     1     4     7
#1     2     5     8
#2     3     6    12
#3     4     9     1
#4     7     5    11

#Notice that the rows starts from 0, like a particular array or list. 
#But the columns starts from 1, as we initially defined.

#Count the Number of Rows and Columns
#shape returns the number of rows and columns
#shape[0] returns the number of rows, we use 0 because we want the first dimension
#shape[1] returns the number of columns, we use 1 because we want the second dimension
count_column = df.shape[1]
print("DataFrame has",count_column, "columns")

count_row = df.shape[0]
print("DataFrame has",count_row, "rows")
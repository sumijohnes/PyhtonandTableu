# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:26:53 2023

@author: sumike
"""

import pandas as pd
data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv",sep=';')


#summary of the data
data.info()

#palying around with varaibles

var = True

#working with calculation
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operation 

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

#Cost per transaction column calculation

#CostPerTransaction = NumberOfItemsPurchased * CostPerItem
#variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfIemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = NumberOfItemsPurchased * CostPerItem

#adding a new column to dataframe

# data['CostPerTransaction'] = CostPerTransaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 

#Markup = (Sales - Cost)/ Cost

data['Markup'] =  data['ProfitPerTransaction']/ data['CostPerTransaction']

#Rounding Marking

roundmarkup = round(data['Markup'],2)
data['Markup']=roundmarkup

#combining data fields
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#checking for column data type
print(data['Day'].dtype)

#Changing column type
day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(day.dtype)


my_date = day +'-'+ data['Month']+'-'+ year

data['Date'] = my_date

# Using iloc to view specific columsn/rows

data.iloc[0] # views the row with index 0
data.iloc[0:3] # first 3 rows
data.iloc[-5:] # last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #all rows 2nd column 
data.iloc[4,2] # 4th row 2nd column

#Using Split function
# new_var = column.str.split('sep' , expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand = True)
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract']=split_col[2]

#using replace function
data['ClientAge']=data['ClientAge'].str.replace('[' , '') # replace opening aquare bracket with nothing
data['LengthOfContract']=data['LengthOfContract'].str.replace(']' , '')

#using the lower function to change item description to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

#merging two files (joining two tables/data frames)

#bringing in a new data set
seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

# syntax: merge_df = pd.merge(df_old,df_new,om = 'key)

data = pd.merge(data,seasons,on = 'Month')

# drop columns
# syntax: df.drop('col_name' , axis = 1) 
data = data.drop('ClientKeywords',axis = 1)
data = data.drop('Day',axis = 1)
data = data.drop('Month',axis = 1)
data = data.drop('Year',axis = 1)

# or data = data.drop(['Day','Year','Month'])

# Export to csv
data.to_csv("ValueInc_Cleaned.csv",index = False)



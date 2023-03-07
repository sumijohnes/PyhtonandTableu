# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:25:00 2023

@author: sumike
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data

json_file = open("loan_data_json.json")
data = json.load(json_file)

#method 2 to read json data

with open("loan_data_json.json") as json_file:
    data = json.load(json_file)
    
# transform to dataframe

loandata = pd.DataFrame(data)

loandata.info()

#finding unque values from purpose column
loandata['purpose'].unique()

#describe data
loandata.describe()

#describe specific columns
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] =  income

# FICO 


''' fico >= 300 and < 400: 'Very Poor'
fico >= 400 and ficoscore < 600: 'Poor'
fico >= 601 and ficoscore < 660: 'Fair'
fico >= 660 and ficoscore < 780: 'Good'
fico >=780: 'Excellent' '''

''' if loandata['fico'] >= 300 and loandata['fico'] < 400:
    loandata['ficocat'] = 'Very Poor'
elif loandata['fico'] >= 400 and loandata['fico'] < 600:
    loandata['ficocat'] = "Poor"
elif loandata['fico'] >= 601 and loandata['fico'] < 660:
    loandata['ficocat'] = "Fair"
elif loandata['fico'] >= 660 and loandata['fico'] < 780:
    loandata['ficocat'] = "Good"
elif loandata['fico'] >= 780:
    loandata['ficocat'] = "Excellent"
else:
    loandata['ficocat'] = 'Unknown' '''
    

#Appying for loops to loandata


length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = "Very Poor"
    elif category >= 400 and category < 600:
        cat = "Poor"
    elif category >= 600 and category < 660:
        cat = "Fair"
    elif category >= 660 and category < 780:
        cat = "Good"
    elif category >= 780:
        cat = "Excellent"
    else:
        cat = "Unknown"
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#Using Exceptions 

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = "Very Poor"
        elif category >= 400 and category < 600:
            cat = "Poor"
        elif category >= 600 and category < 660:
            cat = "Fair"
        elif category >= 660 and category < 780:
            cat = "Good"
        elif category >= 780:
            cat = "Excellent"
        else:
            cat = "Unknown"
    except:
        cat = "Unknown"
        
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[columnname] condition , new column] = value if the condition is met

#for interest rate new column is required. If rate > 0.12 then 'High' else 'low'

loandata.loc[loandata['int.rate'] > 0.12 , 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12 , 'int.rate.type'] = 'Low'

#plots & graphs

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='yellow',width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color="green")
plt.show()

#Scatter plot
xpoint = loandata['dti']
ypoint = loandata['annualincome']
plt.scatter(xpoint,ypoint,color = 'pink')
plt.show()

#writing to csv
loandata.to_csv("loan_cleaned.csv",index = True)


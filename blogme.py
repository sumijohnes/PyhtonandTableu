# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:55:54 2023

@author: sumike
"""

import pandas as pd 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel files
data = pd.read_excel("articles.xlsx")

#summary of the data
data.describe()

#summary of columns
data.info()

#countin the number of articles per source
# group by syntax: df.groupby([column to group])[column to count].count()

data.groupby(['source_id'])['article_id'].count()

# number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()   

#dropping a column
data = data.drop('engagement_comment_plugin_count' , axis=1)

#Functions in python

def thisFunction():
    print('This is my first fucntion')
    
thisFunction()

#This is a function with variables
def aboutMe(name,surname, location):
    print('this is ' +name+" "+surname+". "+"My location is "+location)
    return name,surname,location
    
info = aboutMe("Sumi","Johnes","USA")

#using for loops in functions

def favFood(food):
    for x in food:
        print("top food is "+x)
    
fastfood = ['burgers','pizza','noodles']
favFood(fastfood)

#creating a keyword flag 

''' keyword = 'crash'
length = len(data)
keyword_flag = []
for x in range(0,length):
    heading = data['title'][x]
    if keyword in heading:
        flag = 1
    else:
        flag = 0
        
    keyword_flag.append(flag)
print(keyword_flag) '''
        
#creating a function

def keyWordFlag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
                
        keyword_flag.append(flag)
    return keyword_flag
 
    
keyWordFlag = keyWordFlag('murder')
#print(keyWordFlag)   

#creating new column
data['KeyWordFlag'] = pd.Series(keyWordFlag) 

# SentimentIntensityAnalyzer

sentiment_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sentiment = sentiment_int.polarity_scores(text)

neg = sentiment['neg']
pos = sentiment['pos']
neu = sentiment['neu']

#looping through

neg_sentiment_title = []
pos_sentiment_title = []
neu_sentiment_title = []

length = len(data)
sentiment_int = SentimentIntensityAnalyzer()
for x in range(0,length):
    try:
        text = data['title'][x]
        sentiment = sentiment_int.polarity_scores(text)
        neg = sentiment['neg']
        pos = sentiment['pos']
        neu = sentiment['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    neg_sentiment_title.append(neg)
    pos_sentiment_title.append(pos)
    neu_sentiment_title.append(neu)

# converting to series  creatine new columns

data['neg_sentiment_title'] = pd.Series(neg_sentiment_title)
data['pos_sentiment_title'] = pd.Series(pos_sentiment_title)
data['neu_sentiment_title'] = pd.Series(neu_sentiment_title)


data.to_excel("blogme_clean.xlsx",sheet_name="blogmedata", index = False)


    




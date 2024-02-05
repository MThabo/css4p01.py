# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:48:40 2024

@author: brigh
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")

print(file)
print(file.describe())

print(file['Revenue (Millions)'].mean())
print(file['Rating'].max())
print(file['Title'], file['Year'])
#print(file.sorted_values(by=['Rating'], axis=1))
#print(file[['Title'], file['Rating'] > 9])

sp = file['Title'], file['Year']


#move only title and rating into one dataframe called sp and sorting by ranting

sp = file['Title'], file['Rating']
sp_1 = pd.DataFrame(sp)
print(sp_1.sort_values(by=['Rating'], axis=1))

print(file.describe())

#isolate the revenue and year

clean = file.dropna()

dn = file[['Year' , 'Revenue (Millions)']]

avg = dn.loc[(dn['Year']>= 2015) & (dn['Year']<= 2017)]
print(avg.describe())

total = dn.loc[(dn['Year']== 2016)]
print(total.info())


director = file.loc[(file['Director']== 'Christopher Nolan')]
print(director)

dataset = file.loc[(file['Rating']>= 8)]
print(dataset.info())

print(director['Rating'].median())

hiyeae = file[['Year', 'Rating']]

sorted_df = hiyeae.sort_values(by=['Rating'], ascending=False)
print (sorted_df)

year_range = file.loc[(file['Year']>= 2006) & (file['Year']<= 2016)]

year_range['Growth'] = (year_range['Year']/year_range['Year'].sum())*100

year_range['growth'] = (year_range[:]/year_range['Year'].sum())*100


suit = year_range.sort_values(by=['Year'])
suit['Year'].pct_change()
suit["Growth"]= suit['Year'].pct_change()
print(suit)




year_range.sort_values(by=['Year'])

































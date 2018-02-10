#To begin, what is regression in terms of us using it with machine learning?
#The goal is to take continuous data, find the equation that best fits the data,
#and be able forecast out a specific value. With simple linear regression,
#you are just simply doing this by creating a best fit line
import pandas as pd
import quandl # data frame

df=quandl.get("WIKI/GOOGL") #

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
#adj is just for stock split
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

print(df.head()) # by printing df,head we can see what we are working with

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data
df1 = pd.read_csv("Bengaluru_House_Data.csv")
print(df1.shape)

print(df1)

#investigate area type
#get the count of all area types

print(df1.groupby('area_type')['area_type'].agg('count'))
#looks like area type is not necessary
# drop are un-necessary columns!

df2 = df1.drop(['area_type','society','balcony', 'availability'], axis='columns')

print(df2.head())

#check for null values in all rows
print(df2.isnull().sum())

#drop all rows with null values
df3 = df2.dropna()
#check for null values in all rows
print(df3.isnull().sum())

print(df3.shape)
print(df3.head(20))

#get all unique values in size column
print(df3['size'].unique())
print(df3['size'].unique().size)

#create new column bhk which will contain numberic value from 4 BHK or 4 Bedroom
# or 6 BHK or 6 Bedroom
df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))

print(df3.head())


#get all unique values in size column
print(df3['bhk'].unique())
print(df3['bhk'].unique().size)

#get those rows with bhk > 15
print(df3[df3.bhk > 15])

#get all unique total_sqft
print(df3.total_sqft.unique())
print(df3.total_sqft.unique().size)

#some total_sqft are in range. 

#check all total_sqft values which are pure numbers!

def check_if_float(x):
    try:
        float(x)
    except:
        return False
    return True      

print(df3[df3['total_sqft'].apply(check_if_float)].head(20)      )
print(df3[df3['total_sqft'].apply(check_if_float)].size  )  

#check all total_sqft values which are non-numbers!

print(df3[~df3['total_sqft'].apply(check_if_float)].head(20)  )    
print(df3[~df3['total_sqft'].apply(check_if_float)].size  )  

#convert all total_sqft (in range) to single float values (avg)
def convert_sqft_range_to_float(x):
    temp = x.split('-')
    if(len(temp) == 2):
        return (float(temp[0])+float(temp[1]))/2
    try:
        return float(x)    
    except:
        return None    

df4 = df3
df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_range_to_float) 

print(df4.head(40))

print(df4.loc[137])
print(df4.loc[648])

#ADD NEW COLUMN FOR price_per_sqft
df5 = df4.copy()
df5['price_per_sqft']=df5['price']*100000/df5['total_sqft']
print(df5.head(40))
print(df5.shape)

#get unique values from location column
print(df5.location.unique().size)

df5.location = df5.location.apply(lambda x: x.strip())

#group by location 

print(df5.groupby('location')['location'].agg('count'))

#ascending 
print(df5.groupby('location')['location'].agg('count').sort_values(ascending=False))

#get all locations with less than 10 homes/rows

filter = df5.groupby('location')['location'].agg('count').sort_values(ascending=False)
print(filter)

print(len(filter[filter<=10]))
all_locations_with_houses_less_than10 = filter[filter<=10]
print(all_locations_with_houses_less_than10)
#rename all location with houses less than 10 to others

df5.location = df5.location.apply(lambda x: 'other' if x in all_locations_with_houses_less_than10 else x)

print(df5.location.unique())
print(df5.location.unique().size)
print(df5.head())
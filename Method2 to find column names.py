# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:04:04 2021

@author: 764523
"""

import numpy as np
import pandas as pd

New=pd.read_csv("Newoutputdata.csv")
New1=New.iloc[:,1:]
New2=pd.DataFrame.drop_duplicates(New1)
New3=New2.dropna(axis=1,how="all")

file=pd.read_table("2020_Main_Roll_values_assessed_val_E12V1.tab")
file1=pd.DataFrame.drop_duplicates(file)
file2=file1.dropna(axis=1,how="all")
file3_dup1=file2.drop_duplicates(subset=['PARCELNUMBER'])
#file3_dup2=file2.drop_duplicates(subset=['PARCELNUMBER'])

'''
data = {
    'Pet': ['Cat', 'Dog', 'Dog', 'Dog', 'Cat'],
    'Color': ['Brown', 'Golden', 'Golden', 'Golden', 'Black'],
    'Eyes': ['Black', 'Black', 'Black', 'Brown', 'Green']
}

df = pd.DataFrame(data)

# print the dataframe
print("The original dataframe:\n")
print(df)

# drop duplicates
df_unique = df.drop_duplicates(subset=['Pet', 'Color'])
print("\nAfter dropping duplicates:\n")
print(df_unique)
'''

#assuming parcel numbers are known
column1=New3["pcl"]
column2=file3_dup1["PARCELNUMBER"]

#Common parcel numbers
column1_list=column1.tolist()
column2_list=column2.tolist()
common_elements = set(column1_list).intersection(column2_list)

#Filtering the datset using common parcel numbers
newdf1 = New3[New3.pcl.isin(common_elements)]
newdf2 = file3_dup1[file3_dup1.PARCELNUMBER.isin(common_elements)]

#Dropping the empty columns
newdf11=newdf1.dropna(axis=1,how="all")
newdf21=newdf2.dropna(axis=1,how="all")
#newdf12=newdf11.iloc[:,1:]
newdf11_sorted = newdf11.sort_values(by='pcl')
newdf21_sorted = newdf21.sort_values(by='PARCELNUMBER')

op=newdf11_sorted.reset_index(drop=True)
ip=newdf21_sorted.reset_index(drop=True)
#newdf11_sorted.pcl.to_csv('check1.csv') 
#newdf21_sorted.PARCELNUMBER.to_csv('check2.csv')


len1=len(newdf11_sorted.columns)
len2=len(newdf21_sorted.columns)

Matching=[]
for i in range(len1):
    for j in range(len2):
        a=pd.DataFrame(op.iloc[:,i])
        b=pd.DataFrame(ip.iloc[:,j])
        IM = pd.concat([a,b],axis=1)
        IM1 = IM.dropna(axis=0)
        IM2=sum(IM1.eq(IM1.iloc[:, 0], axis=0).all(1))
        Matching.append(IM2)
        print(i,j,Matching[-1])
 
x = [Matching[i:i + len2] for i in range(0, len(Matching), len2)]  
df_x=pd.DataFrame(x)
df_x.columns=ip.columns
df_x["Rowheader"]=op.columns
cols = list(df_x.columns)
cols = [cols[-1]] + cols[:-1]
df_x = df_x[cols]
df_x.to_csv('Matching.csv') 









#a1=pd.DataFrame(op.iloc[:,1])
#b1=pd.DataFrame(ip.iloc[:,0])
#IM1 = pd.concat([a1,b1],axis=1)
#IM11 = IM1.dropna(axis=0)
#IM21=sum(IM11.eq(IM11.iloc[:, 0], axis=0).all(1))
#Matching.append(IM12)


       
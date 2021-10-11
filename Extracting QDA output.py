# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:43:11 2021

@author: 764523
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:56:29 2020

@author: 764523
"""
import pandas as pd
#df=pd.read_table("2020_Main_Roll_values_assessed_val_E12V1.tab")

#Extracting data from output header file#
import xml.etree.ElementTree as ET 
tree = ET.parse('MS053.fmt') 
root = tree.getroot() 

Field_names=[]
Field_sizes=[]
Field_types=[]
for Field in root.findall('Field'):
    name = Field.get('name')
    Field_names.append(name)
    Size = Field.get('size')
    Field_sizes.append(Size)
    Type = Field.get('type')
    Field_types.append(Type)

from pandas import DataFrame
df1=DataFrame(Field_names,columns=["Headers"])
df2=DataFrame(Field_sizes,columns=["Length"])
df=pd.concat([df1,df2],axis=1)
df["Length"]=df["Length"].astype(int)
df["End Position"]=df["Length"].cumsum(axis=0)
df["Next start Position"]=df["Length"].cumsum(axis=0)+1
df["Start Position"]=df["Next start Position"]-df["Length"]



#Data from outeput records file#
f1 = open("MS053.cv","r")
f11 =f1.read()


    

#Splitting the string into chunks of data(seperate record)#
n=sum(df.Length)
chunks=[f11[i:i+n] for i in range(0,len(f11),n)]



#splitting the chunks of data into seperate coulmns recordwise##
data=[]
test_split=chunks
cus_lens=df["Length"].astype(int)
for i in range(len(chunks)):
    stritr = iter(test_split[i]) 
    res = ["".join(next(stritr) for idx in range(size)) for size in cus_lens] 
    res1 = [x.strip(' ') for x in res]
    data.append(res1)


    


#Attaching the headers to the records#   
data_intermediate=pd.DataFrame(data)
data_intermediate.columns=Field_names

    
#data_intermediate.dtypes=Field_types
data_intermediate.to_csv('Newoutputdata_Humphreys.csv') 


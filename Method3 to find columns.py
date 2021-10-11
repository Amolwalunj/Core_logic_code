# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:30:14 2021

@author: 764523
"""
x1="Newoutputdata.csv"
x2="2020_Main_Roll_values_assessed_val_E12V1.tab"
x3="pcl"
x4="PARCELNUMBER"

from datetime import datetime
import numpy as np
import pandas as pd
init_time = datetime.now()
Newoutputfile=pd.read_csv(x1)
file1=pd.read_table(x2)
Newoutputfile111=Newoutputfile.iloc[:,1:]
Newoutputfile11=pd.DataFrame.drop_duplicates(Newoutputfile111)
Newoutputfile2=Newoutputfile11.dropna(axis=1,how="all")
file1new=file1.dropna(axis=1,how="all")
#assuming parcel numbers are known
column1=Newoutputfile[x3]
column2=file1[x4]

#Common parcel numbers
column1_list=column1.tolist()
column2_list=column2.tolist()
common_elements = set(column1_list).intersection(column2_list)

#Filtering the datset using common parcel numbers
newdf1 = Newoutputfile[Newoutputfile[x3].isin(common_elements)]
newdf2 = file1[file1[x4].isin(common_elements)]

#Dropping the empty columns
newdf11=newdf1.dropna(axis=1,how="all")
newdf21=newdf2.dropna(axis=1,how="all")
newdf12=newdf11.iloc[:,1:]


#import numpy as np
common_elements1 = np.intersect1d(column1_list, column2_list)  
#common_elements = set(column1_list).intersection(column2_list)



#Finding the lengths of common elements
length=[]
for i in range(len(common_elements1)):
    s=((newdf12[(newdf12[x3]==common_elements1[i])]).dropna(axis=1,how="all")).iloc[0].tolist()
    t=((newdf21[(newdf21[x4]==common_elements1[i])]).dropna(axis=1,how="all")).iloc[0].tolist()
    common_elements2 = set(s).intersection(t)
    length.append(len(common_elements2))
    print(i,length[-1])

#Finding the row with maximum common values
Maxlength=max(length)

#To find the index with maximum length
index = length.index(Maxlength)


##To find the columns which have common values
u=((newdf12[(newdf12[x3]==common_elements1[index])]).dropna(axis=1,how="all"))
v=((newdf21[(newdf21[x4]==common_elements1[index])]).dropna(axis=1,how="all"))
    


#Finding the common element values
import numpy as np
u_list=[u.values.tolist()][0][0]
v_list=[v.values.tolist()][0][0]
common_elements11 = [value for value in u_list if value in v_list] 


#Finding the column names with matching values
a_list=[]
b_list=[]
c_list=[]
for i in range(len(common_elements11)):
    a=u.columns[(u == common_elements11[i]).iloc[0]]
    b=v.columns[(v == common_elements11[i]).iloc[0]]
    a_list.append(a)
    b_list.append(b)
    c_list.append(common_elements11[i])
d={"a":a_list,"b":b_list,"c":c_list}
e=pd.DataFrame(d)
e.to_csv('Adams_2020_Main_Roll_values_assessed_val_E12V1_Method3 Matching.csv') 
fin_time = datetime.now()
print("Execution time : ", (fin_time-init_time))
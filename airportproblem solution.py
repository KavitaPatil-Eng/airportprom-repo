# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:48:45 2021

@author: HP
"""
import csv
import json
dict1={}
f=open("airlines.csv","r")
k=csv.reader(f)
data=list(k)
del data[0]

for rec in data:
    print(rec)
    print(" ")
    if rec[1] in dict1:
        dict1[rec[1]]+=1
    else:
        dict1[rec[1]]=1
y=json.dumps(dict1)
print("unique airport names and number of times they repeated:")   
print(" ")
print(y)
print(" ")  


maxvalue=max(dict1,key=dict1.get)
print("The airport which is mentioned the most number of time is: ",maxvalue)
print(" ")

minvalue=min(dict1,key=dict1.get)
print("The airport which is mentioned the least number of  time is : ",minvalue)
      
    

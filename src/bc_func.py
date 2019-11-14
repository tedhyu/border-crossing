# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:46:54 2019

@author: Ted
"""
import csv
from datetime import datetime
import math

def normal_round(n):
    #round function to make sure rounding goes up
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def open_csv(importname):
    list1=[]
    #list1 created from csv
    with open(importname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #row 3,4,5,6 useful
                #they are Border, Date, Measure, Value
                newDate=datetime.strptime(row[4], '%m/%d/%Y %I:%M:%S %p')
                list1.append((row[3],row[5],newDate,row[6]))
                line_count += 1
    #sort in order of Border, Measure, Date, Value
    list1 = sorted(list1, key = lambda x: (x[0], x[1], x[2], x[3]))
    return list1




def combine_value(list1):
    Border=''
    Date=''
    Measure=''
    Value=0    
    #list2 combines values for rows where Border, Date, Measure are the same, creating new "Value"
    list2=[]
    for row2 in list1:        
        if row2[0]==Border and row2[1]==Measure and row2[2]==Date:
            Value=Value+int(row2[3])
            list2.pop()
            list2.append((Border, Measure, Date, Value))
        else:  
            Border=row2[0]
            Measure=row2[1]
            Date=row2[2]
            #Date=row2[2]
            Value=int(row2[3])
            list2.append((Border, Measure, Date, Value)) 
    return list2
            
def calc_average(list2):
    #list3 creates running total by previous month when Border and Measure are the same, creating "Average"
    Border=''
    Measure=''
    list3=[]
    Running_Value=0
    run_month_count=0
    for row3 in list2:
        if row3[0]==Border and row3[1]==Measure:
            run_month_count+=1
            Average=normal_round(Running_Value/run_month_count)
            Running_Value=Running_Value+row3[3]
            list3.append((row3[0],row3[2],row3[1],row3[3],Average))

            
        else:
            Border=row3[0]
            Measure=row3[1]
            Running_Value=row3[3]
            run_month_count=0  #set the number of months to zero when the border and measure are not duplicates
            list3.append((row3[0],row3[2],row3[1],row3[3],0))

    #sort list3 accordignly to Date, Value, Measure, and Border according to rules    
    list3 = sorted(list3, key = lambda x: (x[1], x[3], x[2], x[0]), reverse=True)
    return list3   

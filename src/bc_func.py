###################################
# Definitions
###################################

import csv
from datetime import datetime
import math

def normal_round(n):
    """
    Rounds a number n so that 0.5 will always round up.
    param: n: a float to be rounded
    output: n: a rounded integer
    """
    #round function to make sure rounding goes up
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def open_csv(importname):
    """
    The input csv is opened with the csv module.  Possible commas within quotation marks will not affect the code.  
    The four columns are Border, Measure, Date, and Value.  They are sorted by Border -> Measure -> Date.  
    The sorting allows data from the same border, measure and date to be aggregated.  This allows the
    program to add the value of the aggregated rows together without having to save these values separately. 
    The date is changed to datetime so that it will not be ordered incorrectly.
    param: importname: the name of the input file, e.g. Border-Crossing-Entry-Data.csv
    output: list1:  A sort list of four columns of the input in the order of Border, Measure, Date, Value
    """
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
    #sort in order of Border, Measure, Date
    list1 = sorted(list1, key = lambda x: (x[0], x[1], x[2]))
    return list1

def combine_value(list1):
    """
    The program runs through the rows of a list that has aggregated rows of identical Border, Measure, and Date.  
    The code adds the values of the aggregated rows.  All of the rows of similar Border, Measure, and Date are then
    combined.  The resulting rows of the list are still aggregated by Border and Measure in preparation for the next
    function of calculating the average.
    param: list1: four column list of Border, Measure, Date, and Value that are ordered so that similar columns are aggregated.
    output: list2:  four column list of Border, Measure, Date, and Value where the rows of similar Border, Measure, and Date are combined.
    """
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
    """
    The program runs through the rows of a list that has aggregated rows of identical Border and Measure.  The aggregated rows are also
    ordered sequentially from earliest to latest date.  As the program processes each row, it will keep a running total of the value
    for a unique Border and Measure.  If the next row has the same Border and measure, the program will add the newest value to the running
    total.  It will then display the average of the running total divided by the total months.  If there is no running total, it will enter
    a value of zero for the average.  
    
    The last step is the order the list by the desired output format by the order of Date, Value, Measure, and Border by reverse chronological
    order.
    
    param: list1: four column list of Border, Measure, Date, and Value that are ordered by date and aggregated by Border and Measure.
    output: list2:  five column list of Border, Date, Measure, Value, and Average reversely ordered by Date, Value, Measure, and Date.
    """
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

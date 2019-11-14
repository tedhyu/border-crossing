###################################
# @author: Ted Yu
# @version: v1.0
# INSIGHT DATA ENGINEERING CODING CHALLENGE
# Challenge:
# The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, 
# equipment, passengers and pedestrians crossing into the United States by land.

# For this challenge, the code calculates the total number of times vehicles, equipment, passengers 
# and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. The code also calculates
# the running monthly average of total number of crossings for that type of crossing and border.
###################################


###################################
# Imports
###################################
import sys
import bc_func as bf


###################################
# Presets
###################################

importname=sys.argv[1]
exportname=sys.argv[2]


###################################
# Main
###################################
    
list1=bf.open_csv(importname)
list2=bf.combine_value(list1)
list3=bf.calc_average(list2)

#export list3 to report.csv
with open(exportname, 'w') as out_f:
    out_f.write('Border,Date,Measure,Value,Average\n')
    for l in list3:
        l=l[0]+','+l[1].strftime('%m/%d/%Y %I:%M:%S %p')+','+l[2]+','+str(l[3])+','+str(l[4])+'\n'
        #change date back to original format
        out_f.write(l)
        


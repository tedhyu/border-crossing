###################################
# Border Crossing aggregation demonstration
# Ted Yu, 2019
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
        out_f.write(l)
        


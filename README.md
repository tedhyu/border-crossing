# Scripts for Insight Data Engineering coding challenge
This GitHub repository contains my solution to the [coding challenge](https://github.com/InsightDataScience/border-crossing-analysis) for the Fellows Program organized by [Insight Data Science](https://www.insightdatascience.com/).

Given a comma separated input file with 5 columns, e.g.,

```
Port Name,State,Port Code,Border,Date,Measure,Value,Location
Derby Line,Vermont,209,US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,POINT (-72.09944 45.005)
Norton,Vermont,211,US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,POINT (-71.79528000000002 45.01)
Calexico,California,2503,US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,POINT (-115.49806000000001 32.67889)
Hidalgo,Texas,2305,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,156891,POINT (-98.26278 26.1)
Frontier,Washington,3020,US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,POINT (-117.78134000000001 48.910160000000005)
Presidio,Texas,2403,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,15272,POINT (-104.37167 29.56056)
Eagle Pass,Texas,2303,US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,POINT (-100.49917 28.70889)
```
The script generates a list of Port, Month, Measure, Crossings, and Running Average for each category of border crossing.  
```
Border,Date,Measure,Value,Average
US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,114487
US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,0
US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,0
US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,172163,56810
US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,0
US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,0
```
## Summary
The `pharmacy_counting.py` script reads the input file line by line and creates two dictionaries `drug_cost` (i.e, `{drug_name:total_cost, }`) to keep track of drug costs and `doctor_names` (i.e., `{drug_name:unique_doctor_names}`) to keep track of unique doctor names for each drug. Consequently, the dictionary `drug_cost` is sorted by the value (and key if there is a tie) and written in the desired comma separated output format. This script also performs a basic data cleaning such as getting rid of commas inside quotations. This ensures each row has 5 columns when split on commas.

## Instructions
To execute the script move to the main directory of the project and run the following in the terminal:

```
python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
```

Last two arguments should be input and output files, respectively.

Alternatively, you can execute `./run.sh` script to run the codes for a sample file and perform a unit test.
